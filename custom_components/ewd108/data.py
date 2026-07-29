"""Custom runtime types for EWD108."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import Ewd108ModbusClient
    from .coordinator import Ewd108DataUpdateCoordinator


type Ewd108ConfigEntry = ConfigEntry[Ewd108Data]


@dataclass
class Ewd108Data:
    """Data for the EWD108 integration."""

    client: Ewd108ModbusClient
    coordinator: Ewd108DataUpdateCoordinator
    integration: Integration
