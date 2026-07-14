"""Observability utility exceptions."""

from ai_observability.base.exceptions import (
    ObservationError,
)


class UtilityError(ObservationError):
    """Raised when an observability utility operation fails."""
