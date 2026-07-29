"""Binary sensor platform for EWD108."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorEntityDescription

from .entity import Ewd108Entity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import Ewd108DataUpdateCoordinator
    from .data import Ewd108ConfigEntry

ENTITY_DESCRIPTIONS = (
    BinarySensorEntityDescription(
        key="fix_valid",
        name="Fix valid",
        icon="mdi:satellite-variant",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: Ewd108ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the binary_sensor platform."""
    async_add_entities(
        Ewd108BinarySensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class Ewd108BinarySensor(Ewd108Entity, BinarySensorEntity):
    """EWD108 binary sensor class."""

    def __init__(
        self,
        coordinator: Ewd108DataUpdateCoordinator,
        entity_description: BinarySensorEntityDescription,
    ) -> None:
        """Initialize the binary_sensor class."""
        super().__init__(coordinator, entity_description.key)
        self.entity_description = entity_description

    @property
    def is_on(self) -> bool:
        """Return true if the binary_sensor is on."""
        if self.coordinator.data is None:
            return False
        return bool(self.coordinator.data.get("fix_valid", False))
