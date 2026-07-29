"""Shared entity classes for EWD108."""

from __future__ import annotations

from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    CONF_CONNECTION_TYPE,
    CONF_SERIAL_PORT,
    CONF_SLAVE_ID,
    CONNECTION_TYPE_SERIAL,
    DOMAIN,
    MANUFACTURER,
    MODEL,
)
from .coordinator import Ewd108DataUpdateCoordinator


class Ewd108Entity(CoordinatorEntity[Ewd108DataUpdateCoordinator]):
    """Base entity for all EWD108 entities."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: Ewd108DataUpdateCoordinator, key: str) -> None:
        """Initialize."""
        super().__init__(coordinator)
        connection_type = coordinator.config_entry.data.get(CONF_CONNECTION_TYPE)
        if connection_type == CONNECTION_TYPE_SERIAL:
            endpoint = coordinator.config_entry.data.get(CONF_SERIAL_PORT, "unknown")
        else:
            host = coordinator.config_entry.data.get(CONF_HOST, "unknown")
            port = coordinator.config_entry.data.get(CONF_PORT, "unknown")
            endpoint = f"{host}:{port}"

        slave = coordinator.config_entry.data.get(CONF_SLAVE_ID, "unknown")

        self._attr_unique_id = f"{coordinator.config_entry.entry_id}_{key}"
        self._attr_device_info = DeviceInfo(
            identifiers={
                (
                    DOMAIN,
                    f"{endpoint}_{slave}",
                ),
            },
            manufacturer=MANUFACTURER,
            model=MODEL,
            name=f"EWD108 slave {slave}",
        )
