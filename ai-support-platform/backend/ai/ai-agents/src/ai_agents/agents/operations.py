from __future__ import annotations

from ai_agents.base.operations import (
    AgentInput,
    AgentOutput,
    BaseAgent,
)

from .constants import (
    DEFAULT_AGENT_DESCRIPTION,
    DEFAULT_AGENT_NAME,
)


class SimpleAgent(BaseAgent):
    """A simple concrete implementation of BaseAgent."""

    def __init__(
        self,
        name: str = DEFAULT_AGENT_NAME,
        description: str = DEFAULT_AGENT_DESCRIPTION,
    ) -> None:
        self._name = name
        self._description = description

    @property
    def name(self) -> str:
        """Return the agent name."""
        return self._name

    @property
    def description(self) -> str:
        """Return the agent description."""
        return self._description

    async def run(
        self,
        agent_input: AgentInput,
    ) -> AgentOutput:
        """Execute the agent.

        Currently returns the received message.
        """
        return AgentOutput(
            response=agent_input.message,
        )
