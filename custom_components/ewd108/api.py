"""Modbus client and RMC parser for EWD108 devices."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from math import atan2, cos, radians, sin, sqrt
from typing import Any

from pymodbus.client import AsyncModbusSerialClient, AsyncModbusTcpClient
from pymodbus.exceptions import ModbusException

try:
    from pymodbus import FramerType
except Exception:  # pragma: no cover - depends on pymodbus version
    FramerType = None

from .const import (
    CONNECTION_TYPE_RTU_OVER_TCP,
    CONNECTION_TYPE_SERIAL,
    CONNECTION_TYPE_TCP,
    RMC_REGISTER_ADDRESS,
    RMC_REGISTER_COUNT,
)


class Ewd108ClientError(Exception):
    """Base class for EWD108 client errors."""


class Ewd108ClientCommunicationError(Ewd108ClientError):
    """Raised when communication with the device fails."""


class Ewd108ClientParseError(Ewd108ClientError):
    """Raised when the RMC payload cannot be parsed."""


@dataclass(slots=True)
class Ewd108RmcData:
    """Parsed RMC data returned to the coordinator."""

    fix_valid: bool
    raw_rmc: str
    timestamp_utc: datetime | None
    latitude: float | None
    longitude: float | None
    speed_knots: float | None
    speed_kmh: float | None
    speed_m_s: float | None
    course: float | None
    geohash: str | None
    position_text: str | None


class Ewd108ModbusClient:
    """Read and parse EWD108 RMC data over Modbus RTU."""

    def __init__(
        self,
        connection_type: str,
        host: str | None,
        port: int | str,
        serial_port: str | None,
        baudrate: int,
        bytesize: int,
        parity: str,
        stopbits: int,
        slave_id: int,
        delay: float,
        timeout: int,
    ) -> None:
        """Initialize Modbus client settings."""
        self._connection_type = connection_type
        self._host = host
        self._port = port
        self._serial_port = serial_port
        self._baudrate = baudrate
        self._bytesize = bytesize
        self._parity = parity
        self._stopbits = stopbits
        self._slave_id = slave_id
        self._delay = delay
        self._timeout = timeout
        self._client: AsyncModbusSerialClient | AsyncModbusTcpClient | None = None

    async def async_close(self) -> None:
        """Close the Modbus connection if opened."""
        if self._client is not None:
            self._client.close()
            self._client = None

    async def async_get_data(self) -> dict[str, Any]:
        """Read and parse one RMC frame from the device."""
        try:
            client = await self._async_ensure_client()
        except Ewd108ClientError:
            raise
        except Exception as err:  # pylint: disable=broad-except
            raise Ewd108ClientCommunicationError(
                f"Unable to open Modbus connection: {err}"
            ) from err

        try:
            response = await client.read_holding_registers(
                address=RMC_REGISTER_ADDRESS,
                count=RMC_REGISTER_COUNT,
                slave=self._slave_id,
            )
        except ModbusException as err:
            raise Ewd108ClientCommunicationError(f"Modbus read failed: {err}") from err
        except Exception as err:  # pylint: disable=broad-except
            raise Ewd108ClientCommunicationError(f"Unexpected Modbus error: {err}") from err

        if response.isError():
            raise Ewd108ClientCommunicationError(
                f"Modbus exception response: {response}"
            )

        registers = getattr(response, "registers", None)
        if not registers:
            raise Ewd108ClientCommunicationError("No registers returned by device")

        raw_payload = _decode_registers_to_ascii(registers)
        sentence = _extract_rmc_sentence(raw_payload)
        parsed = _parse_rmc_sentence(sentence)

        return {
            "fix_valid": parsed.fix_valid,
            "raw_rmc": parsed.raw_rmc,
            "timestamp_utc": parsed.timestamp_utc,
            "latitude": parsed.latitude,
            "longitude": parsed.longitude,
            "speed_knots": parsed.speed_knots,
            "speed_kmh": parsed.speed_kmh,
            "speed_m_s": parsed.speed_m_s,
            "course": parsed.course,
            "geohash": parsed.geohash,
            "position_text": parsed.position_text,
        }

    async def _async_ensure_client(self) -> AsyncModbusSerialClient | AsyncModbusTcpClient:
        """Create and connect the Modbus client on first use."""
        if self._client is None:
            self._client = self._create_client()

        if not getattr(self._client, "connected", False):
            is_connected = await self._client.connect()
            if not is_connected:
                raise Ewd108ClientCommunicationError(
                    "Unable to connect to Modbus endpoint"
                )

        return self._client

    def _create_client(self) -> AsyncModbusSerialClient | AsyncModbusTcpClient:
        """Create a pymodbus client for selected transport."""
        if self._connection_type == CONNECTION_TYPE_SERIAL:
            if not self._serial_port:
                raise Ewd108ClientCommunicationError(
                    "Serial port is required for serial transport"
                )
            return AsyncModbusSerialClient(
                port=self._serial_port,
                baudrate=self._baudrate,
                bytesize=self._bytesize,
                parity=self._parity,
                stopbits=self._stopbits,
                timeout=self._timeout,
            )

        if not self._host:
            raise Ewd108ClientCommunicationError("Host is required for TCP transport")

        client_kwargs: dict[str, Any] = {
            "host": self._host,
            "port": int(self._port),
            "timeout": self._timeout,
        }

        if self._connection_type == CONNECTION_TYPE_RTU_OVER_TCP:
            if FramerType is not None:
                client_kwargs["framer"] = FramerType.RTU
            else:
                client_kwargs["framer"] = "rtu"

        if self._delay > 0:
            client_kwargs["reconnect_delay"] = self._delay

        if self._connection_type in {CONNECTION_TYPE_TCP, CONNECTION_TYPE_RTU_OVER_TCP}:
            return AsyncModbusTcpClient(**client_kwargs)

        raise Ewd108ClientCommunicationError(
            f"Unsupported connection type: {self._connection_type}"
        )


def _decode_registers_to_ascii(registers: list[int]) -> str:
    """Decode Modbus register values to ASCII payload."""
    payload = bytearray()
    for register in registers:
        payload.append((register >> 8) & 0xFF)
        payload.append(register & 0xFF)

    return payload.decode("ascii", errors="ignore").replace("\x00", "")


def _extract_rmc_sentence(payload: str) -> str:
    """Extract one RMC sentence from the Modbus payload."""
    if "$" not in payload:
        raise Ewd108ClientParseError("No NMEA sentence start marker in payload")

    for segment in payload.split("$"):
        if "RMC" not in segment:
            continue

        candidate = f"${segment.strip()}"
        candidate = candidate.split("\r", 1)[0].split("\n", 1)[0]
        star_index = candidate.find("*")
        if star_index < 0:
            continue

        trimmed = candidate[: star_index + 3]
        if len(trimmed) >= 10:
            return trimmed

    raise Ewd108ClientParseError("No valid RMC sentence found in payload")


def _parse_rmc_sentence(sentence: str) -> Ewd108RmcData:
    """Parse an NMEA RMC sentence into typed fields."""
    _verify_nmea_checksum(sentence)

    body = sentence[1 : sentence.index("*")]
    fields = body.split(",")
    if len(fields) < 10 or not fields[0].endswith("RMC"):
        raise Ewd108ClientParseError("Malformed RMC sentence")

    fix_valid = fields[2].upper() == "A"
    latitude = _parse_nmea_coordinate(fields[3], fields[4], is_latitude=True)
    longitude = _parse_nmea_coordinate(fields[5], fields[6], is_latitude=False)
    speed_knots = _parse_float(fields[7])
    course = _parse_float(fields[8])
    timestamp_utc = _parse_timestamp(fields[9], fields[1])

    speed_kmh = speed_knots * 1.852 if speed_knots is not None else None
    speed_m_s = speed_knots * 0.514444 if speed_knots is not None else None

    geohash = (
        _encode_geohash(latitude, longitude, precision=9)
        if latitude is not None and longitude is not None
        else None
    )
    position_text = (
        _format_position_text(latitude, longitude)
        if latitude is not None and longitude is not None
        else None
    )

    return Ewd108RmcData(
        fix_valid=fix_valid,
        raw_rmc=sentence,
        timestamp_utc=timestamp_utc,
        latitude=latitude,
        longitude=longitude,
        speed_knots=speed_knots,
        speed_kmh=speed_kmh,
        speed_m_s=speed_m_s,
        course=course,
        geohash=geohash,
        position_text=position_text,
    )


def _verify_nmea_checksum(sentence: str) -> None:
    """Validate the NMEA XOR checksum."""
    if not sentence.startswith("$") or "*" not in sentence:
        raise Ewd108ClientParseError("Sentence does not contain a checksum")

    body = sentence[1 : sentence.index("*")]
    checksum_text = sentence[sentence.index("*") + 1 :].strip().upper()
    if len(checksum_text) < 2:
        raise Ewd108ClientParseError("Checksum is missing")

    try:
        expected = int(checksum_text[:2], 16)
    except ValueError as err:
        raise Ewd108ClientParseError("Checksum contains non-hex characters") from err

    calculated = 0
    for char in body:
        calculated ^= ord(char)

    if calculated != expected:
        raise Ewd108ClientParseError(
            f"Checksum mismatch: expected {expected:02X}, calculated {calculated:02X}"
        )


def _parse_timestamp(date_raw: str, time_raw: str) -> datetime | None:
    """Parse RMC date/time into UTC datetime."""
    if len(date_raw) != 6 or len(time_raw) < 6:
        return None

    time_main, _, fractional = time_raw.partition(".")
    if len(time_main) < 6:
        return None

    try:
        day = int(date_raw[0:2])
        month = int(date_raw[2:4])
        year_short = int(date_raw[4:6])
        year = 2000 + year_short if year_short < 80 else 1900 + year_short

        hour = int(time_main[0:2])
        minute = int(time_main[2:4])
        second = int(time_main[4:6])
        microsecond = int((fractional + "000000")[:6]) if fractional else 0

        return datetime(
            year,
            month,
            day,
            hour,
            minute,
            second,
            microsecond,
            tzinfo=timezone.utc,
        )
    except ValueError:
        return None


def _parse_nmea_coordinate(
    value: str,
    direction: str,
    *,
    is_latitude: bool,
) -> float | None:
    """Convert ddmm.mmmmm (or dddmm.mmmmm) to decimal degrees."""
    if not value or not direction:
        return None

    direction = direction.upper()
    if is_latitude and direction not in {"N", "S"}:
        return None
    if not is_latitude and direction not in {"E", "W"}:
        return None

    degree_digits = 2 if is_latitude else 3
    if len(value) < degree_digits + 2:
        return None

    try:
        degrees = float(value[:degree_digits])
        minutes = float(value[degree_digits:])
    except ValueError:
        return None

    decimal = degrees + (minutes / 60.0)
    if direction in {"S", "W"}:
        decimal *= -1.0

    return decimal


def _parse_float(raw: str) -> float | None:
    """Parse a float field, returning None when missing."""
    if raw == "":
        return None
    try:
        return float(raw)
    except ValueError:
        return None


def _format_position_text(latitude: float, longitude: float) -> str:
    """Create a compact human-readable coordinate string."""
    lat_dir = "N" if latitude >= 0 else "S"
    lon_dir = "E" if longitude >= 0 else "W"
    return f"{abs(latitude):.6f} {lat_dir}, {abs(longitude):.6f} {lon_dir}"


def _encode_geohash(latitude: float, longitude: float, precision: int) -> str:
    """Encode coordinates into geohash without external dependencies."""
    base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
    lat_range = [-90.0, 90.0]
    lon_range = [-180.0, 180.0]
    bits = [16, 8, 4, 2, 1]
    bit_index = 0
    value = 0
    geohash = []
    even = True

    while len(geohash) < precision:
        if even:
            mid = (lon_range[0] + lon_range[1]) / 2
            if longitude >= mid:
                value |= bits[bit_index]
                lon_range[0] = mid
            else:
                lon_range[1] = mid
        else:
            mid = (lat_range[0] + lat_range[1]) / 2
            if latitude >= mid:
                value |= bits[bit_index]
                lat_range[0] = mid
            else:
                lat_range[1] = mid

        even = not even
        if bit_index < 4:
            bit_index += 1
        else:
            geohash.append(base32[value])
            bit_index = 0
            value = 0

    return "".join(geohash)


def distance_meters(
    first_latitude: float,
    first_longitude: float,
    second_latitude: float,
    second_longitude: float,
) -> float:
    """Calculate distance between two points on earth in meters."""
    earth_radius_m = 6_371_000.0

    lat1_rad = radians(first_latitude)
    lat2_rad = radians(second_latitude)
    delta_lat = radians(second_latitude - first_latitude)
    delta_lon = radians(second_longitude - first_longitude)

    value = (
        sin(delta_lat / 2) ** 2
        + cos(lat1_rad) * cos(lat2_rad) * sin(delta_lon / 2) ** 2
    )
    great_circle = 2 * atan2(sqrt(value), sqrt(1 - value))
    return earth_radius_m * great_circle
