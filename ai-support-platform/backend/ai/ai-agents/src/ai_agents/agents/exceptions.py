from __future__ import annotations

"""Exceptions for the agents module."""

from ai_agents.base.exceptions import AgentError


class AgentRegistrationError(AgentError):
    """Raised when an agent cannot be registered."""
