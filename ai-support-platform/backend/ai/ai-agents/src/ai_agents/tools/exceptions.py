from __future__ import annotations

"""Exceptions for the tools module."""

from ai_agents.base.exceptions import AgentError


class ToolExecutionError(AgentError):
    """Raised when tool execution fails."""
