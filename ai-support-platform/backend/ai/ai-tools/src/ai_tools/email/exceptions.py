from __future__ import annotations

"""Email tool exceptions."""

from ai_tools.base.exceptions import ToolConfigurationError


class EmailToolError(ToolConfigurationError):
    """Raised when an email operation fails."""
