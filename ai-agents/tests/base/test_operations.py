from ai_agents.base.operations import (
    AgentContext,
    AgentInput,
    AgentOutput,
    BaseAgent,
)


class DummyAgent(BaseAgent):
    @property
    def name(self) -> str:
        return "dummy"

    @property
    def description(self) -> str:
        return "dummy agent"

    async def run(self, agent_input: AgentInput) -> AgentOutput:
        return AgentOutput(response="ok")


def test_agent_input() -> None:
    data = AgentInput(message="hello")

    assert data.message == "hello"
    assert data.context == {}
    assert data.metadata == {}


def test_agent_output() -> None:
    result = AgentOutput(response="world")

    assert result.response == "world"
    assert result.metadata == {}


def test_agent_context() -> None:
    ctx = AgentContext()

    assert ctx.session_id is None
    assert ctx.user_id is None
    assert ctx.variables == {}


def test_dummy_agent_properties() -> None:
    agent = DummyAgent()

    assert agent.name == "dummy"
    assert agent.description == "dummy agent"
