from __future__ import annotations

"""Execution exceptions."""

from ai_agents.base.exceptions import AgentExecutionError


class ExecutionError(AgentExecutionError):
    """Raised when agent execution fails."""
