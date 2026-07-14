import pytest

from ai_agents.agents.operations import SimpleAgent
from ai_agents.base.operations import (
    AgentInput,
    AgentOutput,
)
from ai_agents.execution.exceptions import ExecutionError
from ai_agents.execution.operations import AgentExecutor


@pytest.mark.asyncio
async def test_execute_success() -> None:
    executor = AgentExecutor()
    agent = SimpleAgent()

    result = await executor.execute(
        agent,
        AgentInput(message="hello"),
    )

    assert isinstance(result, AgentOutput)
    assert result.response == "hello"


class FailingAgent(SimpleAgent):
    async def run(
        self,
        agent_input: AgentInput,
    ) -> AgentOutput:
        raise RuntimeError("failure")


@pytest.mark.asyncio
async def test_execute_failure() -> None:
    executor = AgentExecutor()

    with pytest.raises(ExecutionError):
        await executor.execute(
            FailingAgent(),
            AgentInput(message="hello"),
        )
