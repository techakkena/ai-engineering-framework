from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AgentInput:
    """Input supplied to an agent."""

    message: str
    context: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class AgentOutput:
    """Output returned by an agent."""

    response: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class AgentContext:
    """Runtime execution context."""

    session_id: str | None = None
    user_id: str | None = None
    variables: dict[str, Any] = field(default_factory=dict)


class BaseAgent(ABC):
    """Abstract base class for all agents."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the agent name."""

    @property
    @abstractmethod
    def description(self) -> str:
        """Return the agent description."""

    @abstractmethod
    async def run(self, agent_input: AgentInput) -> AgentOutput:
        """Execute the agent."""

    async def initialize(self) -> None:
        """Initialize resources."""

    async def shutdown(self) -> None:
        """Shutdown resources."""

    async def before_run(self, agent_input: AgentInput) -> None:
        """Hook before execution."""

    async def after_run(self, agent_output: AgentOutput) -> None:
        """Hook after execution."""
