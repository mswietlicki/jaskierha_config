"""Modbus client and RMC parser for EWD108 devices."""

from __future__ import annotations

import asyncio
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from math import atan2, cos, isfinite, radians, sin, sqrt
from typing import TYPE_CHECKING, Any

from modbus_connection import ModbusError

if TYPE_CHECKING:
    from modbus_connection import ModbusUnit

from .const import LOGGER, RMC_REGISTER_ADDRESS, RMC_REGISTER_COUNT


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

    def __init__(self, unit: ModbusUnit) -> None:
        """Receive a unit; Home Assistant owns its shared connection."""
        self._unit = unit
        self._read_lock = asyncio.Lock()

    async def async_get_data(self) -> dict[str, Any]:
        """Poll once, retrying read/parse failures after one and two seconds."""
        async with self._read_lock:
            for attempt in range(3):
                try:
                    return await self._async_read_frame()
                except Ewd108ClientError:
                    if attempt == 2:
                        raise
                    LOGGER.debug("Retrying EWD108 frame after attempt %s", attempt + 1)
                    await asyncio.sleep(attempt + 1)
        msg = "Unreachable retry loop"
        raise AssertionError(msg)

    async def _async_read_frame(self) -> dict[str, Any]:
        """Read a complete GPS frame in one serialized Modbus transaction."""
        try:
            registers = await self._unit.read_holding_registers(
                RMC_REGISTER_ADDRESS, RMC_REGISTER_COUNT
            )
        except ModbusError as err:
            msg = f"Modbus read failed: {err}"
            raise Ewd108ClientCommunicationError(msg) from err
        if len(registers) != RMC_REGISTER_COUNT:
            msg = "Incomplete RMC register response"
            raise Ewd108ClientCommunicationError(msg)

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


def _decode_registers_to_ascii(registers: list[int]) -> str:
    """Decode Modbus register values to ASCII payload."""
    payload = bytearray()
    for register in registers:
        payload.append((register >> 8) & 0xFF)
        payload.append(register & 0xFF)

    try:
        return payload.decode("ascii").rstrip("\x00")
    except UnicodeDecodeError as err:
        msg = "Non-ASCII RMC payload"
        raise Ewd108ClientParseError(msg) from err


def _extract_rmc_sentence(payload: str) -> str:
    """Extract one RMC sentence from the Modbus payload."""
    if "$" not in payload:
        msg = "No NMEA sentence start marker in payload"
        raise Ewd108ClientParseError(msg)

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

    msg = "No valid RMC sentence found in payload"
    raise Ewd108ClientParseError(msg)


def _parse_rmc_sentence(sentence: str) -> Ewd108RmcData:
    """Parse an NMEA RMC sentence into typed fields."""
    _verify_nmea_checksum(sentence)

    body = sentence[1 : sentence.index("*")]
    fields = body.split(",")
    if len(fields) < 10 or not re.fullmatch(
        r"[A-Za-z]{2}RMC", fields[0], re.IGNORECASE
    ):
        msg = "Malformed RMC sentence"
        raise Ewd108ClientParseError(msg)

    status = fields[2].upper()
    if status not in {"A", "V"}:
        msg = "Unknown RMC fix status"
        raise Ewd108ClientParseError(msg)
    fix_valid = status == "A"
    # RMC mode N explicitly means no fix, even if the status says A.
    if len(fields) > 12 and fields[12].upper() == "N":
        fix_valid = False
    latitude = _parse_nmea_coordinate(fields[3], fields[4], is_latitude=True)
    longitude = _parse_nmea_coordinate(fields[5], fields[6], is_latitude=False)
    speed_knots = _parse_float(fields[7])
    course = _parse_float(fields[8])
    timestamp_utc = _parse_timestamp(fields[9], fields[1])

    if fix_valid and (latitude is None or longitude is None or timestamp_utc is None):
        msg = "Valid RMC fix has malformed position or timestamp"
        raise Ewd108ClientParseError(msg)
    if not fix_valid:
        latitude = longitude = speed_knots = course = None
    if speed_knots is not None and speed_knots < 0:
        msg = "Negative RMC speed"
        raise Ewd108ClientParseError(msg)
    if course is not None and not 0 <= course <= 360:
        msg = "Invalid RMC course"
        raise Ewd108ClientParseError(msg)

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
        msg = "Sentence does not contain a checksum"
        raise Ewd108ClientParseError(msg)

    body = sentence[1 : sentence.index("*")]
    checksum_text = sentence[sentence.index("*") + 1 :].strip().upper()
    if len(checksum_text) < 2:
        msg = "Checksum is missing"
        raise Ewd108ClientParseError(msg)

    try:
        expected = int(checksum_text[:2], 16)
    except ValueError as err:
        msg = "Checksum contains non-hex characters"
        raise Ewd108ClientParseError(msg) from err

    calculated = 0
    for char in body:
        calculated ^= ord(char)

    if calculated != expected:
        msg = f"Checksum mismatch: expected {expected:02X}, calculated {calculated:02X}"
        raise Ewd108ClientParseError(msg)


def _parse_timestamp(date_raw: str, time_raw: str) -> datetime | None:
    """Parse RMC date/time into UTC datetime."""
    if len(date_raw) != 6 or not date_raw.isdigit() or len(time_raw) < 6:
        return None

    time_main, _, fractional = time_raw.partition(".")
    if (
        len(time_main) != 6
        or not time_main.isdigit()
        or (fractional and not fractional.isdigit())
    ):
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
            tzinfo=UTC,
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
    if not re.fullmatch(r"[0-9]{" + str(degree_digits + 2) + r"}(?:\.[0-9]+)?", value):
        return None

    try:
        degrees = float(value[:degree_digits])
        minutes = float(value[degree_digits:])
    except ValueError:
        return None

    limit = 90 if is_latitude else 180
    if (
        not isfinite(degrees)
        or not isfinite(minutes)
        or not 0 <= minutes < 60
        or not 0 <= degrees <= limit
        or (degrees == limit and minutes != 0)
    ):
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
        value = float(raw)
        return value if isfinite(value) else None
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
    value = min(1.0, max(0.0, value))
    great_circle = 2 * atan2(sqrt(value), sqrt(1 - value))
    return earth_radius_m * great_circle
