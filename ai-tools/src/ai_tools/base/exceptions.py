"""Exceptions for ai_tools."""

from ai_agents.tools.exceptions import (
    ToolExecutionError,
)


class ToolConfigurationError(
    ToolExecutionError,
):
    """Raised when a tool configuration is invalid."""
