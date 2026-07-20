from __future__ import annotations

"""GitHub tool exceptions."""

from ai_tools.base.exceptions import ToolConfigurationError


class GitHubToolError(ToolConfigurationError):
    """Raised when a GitHub operation fails."""
