"""Token usage exceptions."""

from ai_observability.base.exceptions import (
    ObservationError,
)


class TokenUsageError(ObservationError):
    """Raised for token usage errors."""
