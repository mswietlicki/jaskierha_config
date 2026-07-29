"""Adds config flow for EWD108 GNSS integration."""

from __future__ import annotations

from copy import deepcopy

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.config import async_hass_config_yaml
from homeassistant.const import (
    CONF_HOST,
    CONF_PORT,
    CONF_SCAN_INTERVAL,
    CONF_TIMEOUT,
)
from homeassistant.helpers import selector

from .api import (
    Ewd108ClientCommunicationError,
    Ewd108ClientError,
    Ewd108ClientParseError,
    Ewd108ModbusClient,
)
from .const import (
    CONF_BAUDRATE,
    CONF_BYTESIZE,
    CONF_CONNECTION_TYPE,
    CONF_DELAY,
    CONF_HUB_SOURCE,
    CONF_LOCATION_THRESHOLD_METERS,
    CONF_PARITY,
    CONF_SERIAL_PORT,
    CONF_SET_HA_LOCATION,
    CONF_SLAVE_ID,
    CONF_STOPBITS,
    DEFAULT_BAUDRATE,
    DEFAULT_BYTESIZE,
    DEFAULT_CONNECTION_TYPE,
    DEFAULT_DELAY,
    DEFAULT_HOST,
    DEFAULT_LOCATION_THRESHOLD_METERS,
    DEFAULT_PARITY,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_SET_HA_LOCATION,
    DEFAULT_SLAVE_ID,
    DEFAULT_STOPBITS,
    DEFAULT_TCP_PORT,
    DEFAULT_TIMEOUT,
    CONNECTION_TYPE_RTU_OVER_TCP,
    CONNECTION_TYPE_SERIAL,
    CONNECTION_TYPE_TCP,
    DOMAIN,
    LOGGER,
    MAX_SCAN_INTERVAL,
    MAX_SLAVE_ID,
    MIN_SCAN_INTERVAL,
    MIN_SLAVE_ID,
)

DOCUMENTATION_URL = "https://github.com/mswietlicki/HA_EWD108"


class Ewd108FlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for EWD108."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize flow state."""
        self._modbus_hubs: list[dict] = []
        self._selected_hub_defaults: dict = {}

    async def async_step_user(
        self,
        user_input: dict | None = None,
    ) -> config_entries.ConfigFlowResult:
        """Handle initial step selecting existing hub or manual setup."""
        self._modbus_hubs = await self._async_load_modbus_hubs()

        if user_input is not None:
            selected = str(user_input[CONF_HUB_SOURCE])
            if selected == "manual":
                self._selected_hub_defaults = {}
            else:
                hub_name = selected.removeprefix("hub:")
                self._selected_hub_defaults = next(
                    (hub for hub in self._modbus_hubs if hub["name"] == hub_name),
                    {},
                )
            return await self.async_step_connection()

        return self.async_show_form(
            step_id="user",
            data_schema=self._build_hub_source_schema(),
        )

    async def async_step_connection(
        self,
        user_input: dict | None = None,
    ) -> config_entries.ConfigFlowResult:
        """Handle transport and device-specific configuration."""
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                self._validate_values(user_input)
                await self._test_connection(user_input)
            except ValueError:
                errors["base"] = "invalid_config"
            except Ewd108ClientCommunicationError as exception:
                LOGGER.error(exception)
                errors["base"] = "connection"
            except Ewd108ClientParseError as exception:
                LOGGER.error(exception)
                errors["base"] = "invalid_rmc"
            except Ewd108ClientError as exception:
                LOGGER.exception("Unexpected EWD108 client error: %s", exception)
                errors["base"] = "unknown"
            else:
                endpoint = self._endpoint_id(user_input)
                unique_id = f"{user_input[CONF_CONNECTION_TYPE]}_{endpoint}_{user_input[CONF_SLAVE_ID]}"
                await self.async_set_unique_id(
                    unique_id=unique_id,
                )
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title=f"EWD108 {endpoint} slave {user_input[CONF_SLAVE_ID]}",
                    data=user_input,
                )

        return self.async_show_form(
            step_id="connection",
            description_placeholders={
                "documentation_url": DOCUMENTATION_URL,
            },
            data_schema=self._build_schema(user_input),
            errors=errors,
        )

    async def _async_load_modbus_hubs(self) -> list[dict]:
        """Read modbus hubs from configuration.yaml and map supported fields."""
        try:
            config = await async_hass_config_yaml(self.hass)
        except Exception as err:  # pylint: disable=broad-except
            LOGGER.debug("Unable to load YAML config for modbus hubs: %s", err)
            return []

        hubs: list[dict] = []
        for hub in config.get("modbus", []):
            if not isinstance(hub, dict):
                continue

            hub_type = str(hub.get("type", "")).lower()
            if hub_type not in {
                CONNECTION_TYPE_SERIAL,
                CONNECTION_TYPE_TCP,
                CONNECTION_TYPE_RTU_OVER_TCP,
            }:
                continue

            name = str(hub.get("name", "")).strip()
            if not name:
                continue

            mapped: dict = {
                "name": name,
                CONF_CONNECTION_TYPE: hub_type,
                CONF_BAUDRATE: _safe_int(hub.get(CONF_BAUDRATE), DEFAULT_BAUDRATE),
                CONF_BYTESIZE: _safe_int(hub.get(CONF_BYTESIZE), DEFAULT_BYTESIZE),
                CONF_PARITY: str(hub.get(CONF_PARITY, DEFAULT_PARITY)).upper(),
                CONF_STOPBITS: _safe_int(hub.get(CONF_STOPBITS), DEFAULT_STOPBITS),
                CONF_TIMEOUT: _safe_int(hub.get(CONF_TIMEOUT), DEFAULT_TIMEOUT),
                CONF_DELAY: _safe_float(hub.get(CONF_DELAY), DEFAULT_DELAY),
            }

            if hub_type == CONNECTION_TYPE_SERIAL:
                mapped[CONF_SERIAL_PORT] = str(hub.get(CONF_PORT, "")).strip()
            else:
                mapped[CONF_HOST] = str(hub.get(CONF_HOST, "")).strip()
                mapped[CONF_PORT] = _safe_int(hub.get(CONF_PORT), DEFAULT_TCP_PORT)

            hubs.append(mapped)

        return hubs

    def _build_hub_source_schema(self) -> vol.Schema:
        """Build selector for choosing existing modbus hub or manual setup."""
        options = [
            selector.SelectOptionDict(value="manual", label="Manual setup")
        ]
        for hub in self._modbus_hubs:
            options.append(
                selector.SelectOptionDict(
                    value=f"hub:{hub['name']}",
                    label=f"Use existing hub: {hub['name']}",
                )
            )

        default = "manual"
        if self._modbus_hubs:
            default = f"hub:{self._modbus_hubs[0]['name']}"

        return vol.Schema(
            {
                vol.Required(CONF_HUB_SOURCE, default=default): selector.SelectSelector(
                    selector.SelectSelectorConfig(
                        options=options,
                        mode=selector.SelectSelectorMode.DROPDOWN,
                    )
                )
            }
        )

    async def _test_connection(self, user_input: dict) -> None:
        """Validate Modbus connectivity and payload format."""
        client = Ewd108ModbusClient(
            connection_type=user_input[CONF_CONNECTION_TYPE],
            host=user_input.get(CONF_HOST),
            port=user_input.get(CONF_PORT, 0),
            serial_port=user_input.get(CONF_SERIAL_PORT),
            baudrate=user_input[CONF_BAUDRATE],
            bytesize=user_input[CONF_BYTESIZE],
            parity=user_input[CONF_PARITY],
            stopbits=user_input[CONF_STOPBITS],
            slave_id=user_input[CONF_SLAVE_ID],
            delay=float(user_input.get(CONF_DELAY, DEFAULT_DELAY)),
            timeout=user_input[CONF_TIMEOUT],
        )
        try:
            await client.async_get_data()
        finally:
            await client.async_close()

    def _build_schema(self, user_input: dict | None) -> vol.Schema:
        """Build form schema with defaults and selectors."""
        data = deepcopy(self._selected_hub_defaults)
        if user_input:
            data.update(user_input)
        connection_type = data.get(CONF_CONNECTION_TYPE, DEFAULT_CONNECTION_TYPE)

        schema: dict = {
            vol.Required(
                CONF_CONNECTION_TYPE,
                default=connection_type,
            ): vol.In(
                {
                    CONNECTION_TYPE_RTU_OVER_TCP: "RTU over TCP",
                    CONNECTION_TYPE_TCP: "TCP",
                    CONNECTION_TYPE_SERIAL: "Serial RTU",
                }
            )
        }

        if connection_type == CONNECTION_TYPE_SERIAL:
            schema[
                vol.Required(
                    CONF_SERIAL_PORT,
                    default=data.get(CONF_SERIAL_PORT, vol.UNDEFINED),
                )
            ] = str
        else:
            schema[
                vol.Required(
                    CONF_HOST,
                    default=data.get(CONF_HOST, DEFAULT_HOST),
                )
            ] = str
            schema[
                vol.Required(
                    CONF_PORT,
                    default=data.get(CONF_PORT, DEFAULT_TCP_PORT),
                )
            ] = vol.All(vol.Coerce(int), vol.Range(min=1, max=65535))
            schema[
                vol.Required(
                    CONF_DELAY,
                    default=data.get(CONF_DELAY, DEFAULT_DELAY),
                )
            ] = vol.All(vol.Coerce(float), vol.Range(min=0, max=10))

        schema.update(
            {
                vol.Required(
                    CONF_BAUDRATE,
                    default=data.get(CONF_BAUDRATE, DEFAULT_BAUDRATE),
                ): vol.All(vol.Coerce(int), vol.Range(min=1200, max=115200)),
                vol.Required(
                    CONF_BYTESIZE,
                    default=data.get(CONF_BYTESIZE, DEFAULT_BYTESIZE),
                ): vol.All(vol.Coerce(int), vol.In([7, 8])),
                vol.Required(
                    CONF_PARITY,
                    default=data.get(CONF_PARITY, DEFAULT_PARITY),
                ): vol.In(["N", "E", "O"]),
                vol.Required(
                    CONF_STOPBITS,
                    default=data.get(CONF_STOPBITS, DEFAULT_STOPBITS),
                ): vol.All(vol.Coerce(int), vol.In([1, 2])),
                vol.Required(
                    CONF_SLAVE_ID,
                    default=data.get(CONF_SLAVE_ID, DEFAULT_SLAVE_ID),
                ): vol.All(
                    vol.Coerce(int), vol.Range(min=MIN_SLAVE_ID, max=MAX_SLAVE_ID)
                ),
                vol.Required(
                    CONF_SCAN_INTERVAL,
                    default=data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL),
                ): vol.All(
                    vol.Coerce(int),
                    vol.Range(min=MIN_SCAN_INTERVAL, max=MAX_SCAN_INTERVAL),
                ),
                vol.Required(
                    CONF_TIMEOUT,
                    default=data.get(CONF_TIMEOUT, DEFAULT_TIMEOUT),
                ): vol.All(vol.Coerce(int), vol.Range(min=1, max=30)),
                vol.Required(
                    CONF_SET_HA_LOCATION,
                    default=data.get(CONF_SET_HA_LOCATION, DEFAULT_SET_HA_LOCATION),
                ): bool,
                vol.Required(
                    CONF_LOCATION_THRESHOLD_METERS,
                    default=data.get(
                        CONF_LOCATION_THRESHOLD_METERS,
                        DEFAULT_LOCATION_THRESHOLD_METERS,
                    ),
                ): vol.All(vol.Coerce(float), vol.Range(min=1, max=100000)),
            }
        )

        return vol.Schema(schema)

    def _validate_values(self, user_input: dict) -> None:
        """Validate form values before connection test."""
        connection_type = user_input[CONF_CONNECTION_TYPE]
        if connection_type not in {
            CONNECTION_TYPE_SERIAL,
            CONNECTION_TYPE_TCP,
            CONNECTION_TYPE_RTU_OVER_TCP,
        }:
            raise ValueError("Invalid connection type")

        if connection_type == CONNECTION_TYPE_SERIAL:
            if not str(user_input.get(CONF_SERIAL_PORT, "")).strip():
                raise ValueError("Serial port is required")
        else:
            if not str(user_input.get(CONF_HOST, "")).strip():
                raise ValueError("Host is required")
            tcp_port = int(user_input[CONF_PORT])
            if tcp_port < 1 or tcp_port > 65535:
                raise ValueError("Invalid TCP port")

            delay = float(user_input.get(CONF_DELAY, DEFAULT_DELAY))
            if delay < 0:
                raise ValueError("Invalid delay")

        slave_id = int(user_input[CONF_SLAVE_ID])
        if slave_id < MIN_SLAVE_ID or slave_id > MAX_SLAVE_ID:
            raise ValueError("Invalid slave id")

        scan_interval = int(user_input[CONF_SCAN_INTERVAL])
        if scan_interval < MIN_SCAN_INTERVAL or scan_interval > MAX_SCAN_INTERVAL:
            raise ValueError("Invalid scan interval")

        threshold = float(user_input[CONF_LOCATION_THRESHOLD_METERS])
        if threshold <= 0:
            raise ValueError("Invalid location threshold")

    def _endpoint_id(self, user_input: dict) -> str:
        """Create a stable endpoint identifier for title/unique id."""
        if user_input[CONF_CONNECTION_TYPE] == CONNECTION_TYPE_SERIAL:
            return str(user_input.get(CONF_SERIAL_PORT, "serial")).strip()
        return f"{user_input.get(CONF_HOST)}:{user_input.get(CONF_PORT)}"


def _safe_int(value: object, default: int) -> int:
    """Convert a YAML value to int, falling back to a default."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _safe_float(value: object, default: float) -> float:
    """Convert a YAML value to float, falling back to a default."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return default
