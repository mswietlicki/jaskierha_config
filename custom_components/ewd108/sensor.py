"""Sensor platform for EWD108."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import UnitOfSpeed
from homeassistant.helpers.entity import EntityCategory

from .entity import Ewd108Entity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import Ewd108DataUpdateCoordinator
    from .data import Ewd108ConfigEntry


@dataclass(frozen=True, kw_only=True)
class Ewd108SensorEntityDescription(SensorEntityDescription):
    """Description for EWD108 sensors."""

    value_fn: Callable[[dict[str, Any]], Any]


ENTITY_DESCRIPTIONS: tuple[Ewd108SensorEntityDescription, ...] = (
    Ewd108SensorEntityDescription(
        key="latitude",
        name="Latitude",
        icon="mdi:latitude",
        value_fn=lambda data: data.get("latitude"),
    ),
    Ewd108SensorEntityDescription(
        key="longitude",
        name="Longitude",
        icon="mdi:longitude",
        value_fn=lambda data: data.get("longitude"),
    ),
    Ewd108SensorEntityDescription(
        key="speed",
        name="Speed",
        icon="mdi:speedometer",
        native_unit_of_measurement=UnitOfSpeed.KILOMETERS_PER_HOUR,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.get("speed_kmh"),
    ),
    Ewd108SensorEntityDescription(
        key="course",
        name="Course",
        icon="mdi:compass",
        value_fn=lambda data: data.get("course"),
    ),
    Ewd108SensorEntityDescription(
        key="timestamp",
        name="Timestamp",
        device_class=SensorDeviceClass.TIMESTAMP,
        value_fn=lambda data: data.get("timestamp_utc"),
    ),
    Ewd108SensorEntityDescription(
        key="raw_rmc",
        name="Raw RMC",
        icon="mdi:code-braces",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: data.get("raw_rmc"),
    ),
    Ewd108SensorEntityDescription(
        key="geohash",
        name="Geohash",
        icon="mdi:map-marker-radius",
        value_fn=lambda data: data.get("geohash"),
    ),
    Ewd108SensorEntityDescription(
        key="position_text",
        name="Position",
        icon="mdi:map-marker",
        value_fn=lambda data: data.get("position_text"),
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: Ewd108ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities(
        Ewd108Sensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class Ewd108Sensor(Ewd108Entity, SensorEntity):
    """EWD108 sensor class."""

    entity_description: Ewd108SensorEntityDescription

    def __init__(
        self,
        coordinator: Ewd108DataUpdateCoordinator,
        entity_description: Ewd108SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator, entity_description.key)
        self.entity_description = entity_description

    @property
    def native_value(self) -> Any:
        """Return the native value of the sensor."""
        if self.coordinator.data is None:
            return None
        return self.entity_description.value_fn(self.coordinator.data)
