"""Search tool exceptions."""

from ai_tools.base.exceptions import ToolConfigurationError


class SearchToolError(ToolConfigurationError):
    """Raised when a search operation fails."""
