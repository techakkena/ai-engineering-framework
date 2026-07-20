from __future__ import annotations

class AgentError(Exception):
    """Base exception for ai-agents."""


class AgentConfigurationError(AgentError):
    """Raised when an agent configuration is invalid."""


class AgentExecutionError(AgentError):
    """Raised when an agent execution fails."""


class AgentValidationError(AgentError):
    """Raised when agent validation fails."""
