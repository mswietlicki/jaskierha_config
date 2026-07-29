"""
Custom integration to integrate EWD108 GNSS with Home Assistant.

For more details about this integration, please refer to
https://github.com/mswietlicki/HA_EWD108
"""

from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING

from homeassistant.const import (
    CONF_HOST,
    CONF_PORT,
    CONF_SCAN_INTERVAL,
    CONF_TIMEOUT,
    Platform,
)
from homeassistant.loader import async_get_loaded_integration

from .api import Ewd108ModbusClient
from .const import (
    CONF_BAUDRATE,
    CONF_BYTESIZE,
    CONF_CONNECTION_TYPE,
    CONF_DELAY,
    CONF_PARITY,
    CONF_SERIAL_PORT,
    CONF_SLAVE_ID,
    CONF_STOPBITS,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_TIMEOUT,
    DOMAIN,
    LOGGER,
)
from .coordinator import Ewd108DataUpdateCoordinator
from .data import Ewd108Data

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

    from .data import Ewd108ConfigEntry

PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
]


# https://developers.home-assistant.io/docs/config_entries_index/#setting-up-an-entry
async def async_setup_entry(
    hass: HomeAssistant,
    entry: Ewd108ConfigEntry,
) -> bool:
    """Set up this integration using UI."""
    coordinator = Ewd108DataUpdateCoordinator(
        hass=hass,
        logger=LOGGER,
        name=DOMAIN,
        update_interval=timedelta(
            seconds=entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)
        ),
    )
    entry.runtime_data = Ewd108Data(
        client=Ewd108ModbusClient(
            connection_type=entry.data[CONF_CONNECTION_TYPE],
            host=entry.data.get(CONF_HOST),
            port=entry.data.get(CONF_PORT, 0),
            serial_port=entry.data.get(CONF_SERIAL_PORT),
            baudrate=entry.data[CONF_BAUDRATE],
            bytesize=entry.data[CONF_BYTESIZE],
            parity=entry.data[CONF_PARITY],
            stopbits=entry.data[CONF_STOPBITS],
            slave_id=entry.data[CONF_SLAVE_ID],
            delay=float(entry.data.get(CONF_DELAY, 0.0)),
            timeout=entry.data.get(CONF_TIMEOUT, DEFAULT_TIMEOUT),
        ),
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
    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unloaded:
        await entry.runtime_data.client.async_close()
    return unloaded


async def async_reload_entry(
    hass: HomeAssistant,
    entry: Ewd108ConfigEntry,
) -> None:
    """Reload config entry."""
    await hass.config_entries.async_reload(entry.entry_id)
