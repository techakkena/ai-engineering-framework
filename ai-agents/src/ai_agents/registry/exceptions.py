"""Exceptions for the registry module."""

from ai_agents.base.exceptions import AgentError


class AgentAlreadyRegisteredError(AgentError):
    """Raised when attempting to register an existing agent."""


class AgentNotFoundError(AgentError):
    """Raised when an agent cannot be found."""
