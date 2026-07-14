"""Logging exceptions."""

from ai_observability.base.exceptions import (
    ObservationError,
)


class LoggingError(ObservationError):
    """Raised when logging fails."""
