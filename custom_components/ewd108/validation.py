"""Reject stale or implausible complete GPS samples."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from .api import distance_meters

MAX_FIX_AGE_SECONDS = 30
MAX_FUTURE_SECONDS = 5
MAX_SPEED_METERS_PER_SECOND = 250 / 3.6
POSITION_TOLERANCE_METERS = 100


class PositionValidator:
    """Keep the last accepted sample as the outlier baseline."""

    def __init__(self) -> None:
        """Start without a baseline; invalid samples never replace it."""
        self._last_fix: tuple[float, float, datetime] | None = None

    def validate(self, data: dict[str, Any], now: datetime) -> dict[str, Any]:
        """Return a safe copy, preserving raw frame and rejection diagnostics."""
        reason = self._reason(data, now)
        result = {**data, "rejection_reason": reason}
        if reason:
            result.update(
                fix_valid=False,
                latitude=None,
                longitude=None,
                speed_knots=None,
                speed_kmh=None,
                speed_m_s=None,
                course=None,
                geohash=None,
                position_text=None,
            )
        else:
            self._last_fix = (
                data["latitude"],
                data["longitude"],
                data["timestamp_utc"],
            )
        return result

    def _reason(self, data: dict[str, Any], now: datetime) -> str | None:
        """Explain the first failed validation rule."""
        if not data.get("fix_valid"):
            return "invalid_fix"
        lat, lon, timestamp = (
            data.get("latitude"),
            data.get("longitude"),
            data.get("timestamp_utc"),
        )
        if lat is None or lon is None or not isinstance(timestamp, datetime):
            return "incomplete_fix"
        if not -90 <= lat <= 90 or not -180 <= lon <= 180 or (lat == 0 and lon == 0):
            return "invalid_coordinates"
        age = (now - timestamp).total_seconds()
        if age > MAX_FIX_AGE_SECONDS:
            return "stale_fix"
        if age < -MAX_FUTURE_SECONDS:
            return "future_fix"
        if self._last_fix is not None:
            previous_lat, previous_lon, previous_time = self._last_fix
            elapsed = (timestamp - previous_time).total_seconds()
            if elapsed < 0:
                return "out_of_order_fix"
            limit = POSITION_TOLERANCE_METERS + MAX_SPEED_METERS_PER_SECOND * elapsed
            if distance_meters(previous_lat, previous_lon, lat, lon) > limit:
                return "implausible_jump"
        return None
