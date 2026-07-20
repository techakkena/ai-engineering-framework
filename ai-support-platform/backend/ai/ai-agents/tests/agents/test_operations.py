from __future__ import annotations

from ai_agents.agents.operations import SimpleAgent
from ai_agents.base.operations import (
    AgentInput,
)

import asyncio


def test_default_constructor() -> None:
    agent = SimpleAgent()

    assert agent.name == "agent"
    assert "Default" in agent.description


def test_custom_constructor() -> None:
    agent = SimpleAgent(
        name="assistant",
        description="AI Assistant",
    )

    assert agent.name == "assistant"
    assert agent.description == "AI Assistant"


def test_run() -> None:
    agent = SimpleAgent()

    result = asyncio.run(agent.run(AgentInput(message="hello")))

    assert result.response == "hello"
