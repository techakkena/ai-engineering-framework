"""Storage tool exceptions."""

from ai_tools.base.exceptions import ToolConfigurationError


class StorageToolError(ToolConfigurationError):
    """Raised when a storage operation fails."""
