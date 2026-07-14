"""Latency exceptions."""

from ai_observability.base.exceptions import (
    ObservationError,
)


class LatencyError(ObservationError):
    """Raised for latency errors."""
