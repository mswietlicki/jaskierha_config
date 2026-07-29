"""DataUpdateCoordinator for EWD108."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import (
    Ewd108ClientCommunicationError,
    Ewd108ClientError,
    Ewd108ClientParseError,
    distance_meters,
)
from .const import CONF_LOCATION_THRESHOLD_METERS, CONF_SET_HA_LOCATION

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant

    from .data import Ewd108ConfigEntry


# https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
class Ewd108DataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage polling and post-processing EWD108 data."""

    config_entry: Ewd108ConfigEntry

    def __init__(self, hass: HomeAssistant, **kwargs: Any) -> None:
        """Initialize coordinator and sync state."""
        super().__init__(hass=hass, **kwargs)
        self._last_location_sync: tuple[float, float] | None = None
        if hass.config.latitude is not None and hass.config.longitude is not None:
            self._last_location_sync = (hass.config.latitude, hass.config.longitude)

    async def _async_update_data(self) -> Any:
        """Update data via library."""
        try:
            data = await self.config_entry.runtime_data.client.async_get_data()
            await self._async_maybe_update_location(data)
            return data
        except Ewd108ClientCommunicationError as exception:
            raise UpdateFailed(exception) from exception
        except Ewd108ClientParseError as exception:
            raise UpdateFailed(exception) from exception
        except Ewd108ClientError as exception:
            raise UpdateFailed(exception) from exception

    async def _async_maybe_update_location(self, data: dict[str, Any]) -> None:
        """Update HA location when enabled and movement exceeds threshold."""
        if not self.config_entry.data.get(CONF_SET_HA_LOCATION, False):
            return

        if not data.get("fix_valid"):
            return

        latitude = data.get("latitude")
        longitude = data.get("longitude")
        if latitude is None or longitude is None:
            return

        threshold = float(
            self.config_entry.data.get(
                CONF_LOCATION_THRESHOLD_METERS,
                100.0,
            )
        )

        if self._last_location_sync is not None:
            moved = distance_meters(
                self._last_location_sync[0],
                self._last_location_sync[1],
                latitude,
                longitude,
            )
            if moved < threshold:
                return

        await self.hass.services.async_call(
            "homeassistant",
            "set_location",
            {
                "latitude": latitude,
                "longitude": longitude,
            },
            blocking=False,
        )
        self._last_location_sync = (latitude, longitude)
