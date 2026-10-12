"""Publish both GPS coordinates from one accepted coordinator sample."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.device_tracker import SourceType
from homeassistant.components.device_tracker.config_entry import TrackerEntity

from .entity import Ewd108Entity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import Ewd108DataUpdateCoordinator
    from .data import Ewd108ConfigEntry


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001
    entry: Ewd108ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the native GPS tracker."""
    async_add_entities([Ewd108Tracker(entry.runtime_data.coordinator)])


class Ewd108Tracker(Ewd108Entity, TrackerEntity):
    """A GPS position that is unavailable whenever the sample is rejected."""

    _attr_name = "GPS"

    def __init__(self, coordinator: Ewd108DataUpdateCoordinator) -> None:
        """Bind the tracker to the same sample as all GNSS sensors."""
        super().__init__(coordinator, "gps")

    @property
    def available(self) -> bool:
        """Never expose a previous coordinate as a current valid fix."""
        return super().available and bool(
            (self.coordinator.data or {}).get("fix_valid")
        )

    @property
    def source_type(self) -> SourceType:
        """Return GPS as the location source."""
        return SourceType.GPS

    @property
    def latitude(self) -> float | None:
        """Return the accepted sample's latitude."""
        return self.coordinator.data.get("latitude") if self.available else None

    @property
    def longitude(self) -> float | None:
        """Return the accepted sample's longitude."""
        return self.coordinator.data.get("longitude") if self.available else None
