"""Operations for the registry module."""

from __future__ import annotations

from ai_agents.base.operations import BaseAgent

from .exceptions import (
    AgentAlreadyRegisteredError,
    AgentNotFoundError,
)


class AgentRegistry:
    """In-memory registry for AI agents."""

    def __init__(self) -> None:
        self._agents: dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        """Register an agent."""
        if agent.name in self._agents:
            raise AgentAlreadyRegisteredError(
                f"Agent '{agent.name}' is already registered."
            )

        self._agents[agent.name] = agent

    def unregister(self, name: str) -> None:
        """Remove an agent."""
        if name not in self._agents:
            raise AgentNotFoundError(f"Agent '{name}' was not found.")

        del self._agents[name]

    def get(self, name: str) -> BaseAgent:
        """Return a registered agent."""
        try:
            return self._agents[name]
        except KeyError as exc:
            raise AgentNotFoundError(f"Agent '{name}' was not found.") from exc

    def exists(self, name: str) -> bool:
        """Return whether an agent exists."""
        return name in self._agents

    def list(self) -> list[str]:
        """Return registered agent names."""
        return sorted(self._agents.keys())

    def clear(self) -> None:
        """Remove all registered agents."""
        self._agents.clear()

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._agents)
