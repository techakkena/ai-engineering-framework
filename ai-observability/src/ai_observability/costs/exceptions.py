"""Cost exceptions."""

from ai_observability.base.exceptions import (
    ObservationError,
)


class CostError(ObservationError):
    """Raised for cost-related errors."""
