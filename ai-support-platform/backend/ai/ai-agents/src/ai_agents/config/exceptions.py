from __future__ import annotations

"""Configuration exceptions."""

from ai_agents.base.exceptions import AgentConfigurationError


class ConfigurationError(AgentConfigurationError):
    """Raised when an agent configuration is invalid."""
