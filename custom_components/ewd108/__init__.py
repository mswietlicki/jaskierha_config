"""
Custom integration to integrate EWD108 GNSS with Home Assistant.

For more details about this integration, please refer to
https://github.com/mswietlicki/HA_EWD108
"""

from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING

from homeassistant.components.modbus import async_get_unit
from homeassistant.components.modbus.const import DATA_MODBUS_HUBS
from homeassistant.config import async_hass_config_yaml
from homeassistant.const import (
    CONF_SCAN_INTERVAL,
    CONF_TIMEOUT,
    Platform,
)
from homeassistant.exceptions import ConfigEntryError
from homeassistant.loader import async_get_loaded_integration

from .api import Ewd108ModbusClient
from .const import (
    CONF_DELAY,
    CONF_SLAVE_ID,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_TIMEOUT,
    DOMAIN,
    LOGGER,
)
from .coordinator import Ewd108DataUpdateCoordinator
from .data import Ewd108Data
from .transport import (
    LegacyHubConflictError,
    check_legacy_hubs,
    check_running_legacy_hubs,
    connection_params,
)

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

    from .data import Ewd108ConfigEntry

PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.DEVICE_TRACKER,
]


# https://developers.home-assistant.io/docs/config_entries_index/#setting-up-an-entry
async def async_setup_entry(
    hass: HomeAssistant,
    entry: Ewd108ConfigEntry,
) -> bool:
    """Set up this integration using UI."""
    yaml_config = await async_hass_config_yaml(hass)
    try:
        check_legacy_hubs(entry.data, yaml_config.get("modbus", []))
        check_running_legacy_hubs(entry.data, hass.data.get(DATA_MODBUS_HUBS, {}))
    except LegacyHubConflictError as err:
        raise ConfigEntryError(str(err)) from err
    unit = async_get_unit(
        hass, entry, connection_params(entry.data), entry.data[CONF_SLAVE_ID]
    )
    unit.require_timeout(entry.data.get(CONF_TIMEOUT, DEFAULT_TIMEOUT))
    entry.async_on_unload(lambda: unit.require_timeout(None))
    unit.set_message_spacing(float(entry.data.get(CONF_DELAY, 0.0)))
    coordinator = Ewd108DataUpdateCoordinator(
        hass=hass,
        logger=LOGGER,
        name=DOMAIN,
        config_entry=entry,
        update_interval=timedelta(
            seconds=entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)
        ),
    )
    entry.runtime_data = Ewd108Data(
        client=Ewd108ModbusClient(unit),
        integration=async_get_loaded_integration(hass, entry.domain),
        coordinator=coordinator,
    )

    # https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
    await coordinator.async_config_entry_first_refresh()

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: Ewd108ConfigEntry,
) -> bool:
    """Handle removal of an entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def async_reload_entry(
    hass: HomeAssistant,
    entry: Ewd108ConfigEntry,
) -> None:
    """Reload config entry."""
    await hass.config_entries.async_reload(entry.entry_id)
