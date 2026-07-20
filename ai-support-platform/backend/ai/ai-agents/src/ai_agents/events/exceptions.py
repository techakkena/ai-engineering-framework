from __future__ import annotations

"""Exceptions for the events module."""

from ai_agents.base.exceptions import AgentError


class EventError(AgentError):
    """Raised when an event operation fails."""
