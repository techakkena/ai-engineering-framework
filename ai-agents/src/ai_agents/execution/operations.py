"""Execution operations."""

from __future__ import annotations

from ai_agents.base.operations import (
    AgentInput,
    AgentOutput,
    BaseAgent,
)

from .exceptions import ExecutionError


class AgentExecutor:
    """Executes agents."""

    async def execute(
        self,
        agent: BaseAgent,
        agent_input: AgentInput,
    ) -> AgentOutput:
        """Execute an agent."""

        try:
            await agent.initialize()
            await agent.before_run(agent_input)

            output = await agent.run(agent_input)

            await agent.after_run(output)
            await agent.shutdown()

            return output

        except Exception as exc:
            raise ExecutionError(str(exc)) from exc
