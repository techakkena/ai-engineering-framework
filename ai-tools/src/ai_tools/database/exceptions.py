"""Database tool exceptions."""

from ai_tools.base.exceptions import ToolConfigurationError


class DatabaseToolError(ToolConfigurationError):
    """Raised when a database operation fails."""
