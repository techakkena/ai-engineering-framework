"""Tool utility exceptions."""

from ai_tools.base.exceptions import (
    ToolConfigurationError,
)


class UtilityError(
    ToolConfigurationError,
):
    """Raised when a tool utility operation fails."""
