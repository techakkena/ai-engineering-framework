from __future__ import annotations

import pytest

from ai_agents.agents.operations import SimpleAgent
from ai_agents.registry.exceptions import (
    AgentAlreadyRegisteredError,
    AgentNotFoundError,
)
from ai_agents.registry.operations import AgentRegistry


def test_register_agent() -> None:
    registry = AgentRegistry()
    agent = SimpleAgent()

    registry.register(agent)

    assert len(registry) == 1
    assert registry.exists(agent.name)


def test_duplicate_registration() -> None:
    registry = AgentRegistry()
    agent = SimpleAgent()

    registry.register(agent)

    with pytest.raises(AgentAlreadyRegisteredError):
        registry.register(agent)


def test_get_agent() -> None:
    registry = AgentRegistry()
    agent = SimpleAgent()

    registry.register(agent)

    assert registry.get(agent.name) is agent


def test_unregister_agent() -> None:
    registry = AgentRegistry()
    agent = SimpleAgent()

    registry.register(agent)
    registry.unregister(agent.name)

    assert len(registry) == 0


def test_unregister_missing_agent() -> None:
    registry = AgentRegistry()

    with pytest.raises(AgentNotFoundError):
        registry.unregister("missing")


def test_get_missing_agent() -> None:
    registry = AgentRegistry()

    with pytest.raises(AgentNotFoundError):
        registry.get("missing")


def test_list_agents() -> None:
    registry = AgentRegistry()

    registry.register(SimpleAgent(name="a"))
    registry.register(SimpleAgent(name="b"))

    assert registry.list() == ["a", "b"]


def test_clear_registry() -> None:
    registry = AgentRegistry()

    registry.register(SimpleAgent())

    registry.clear()

    assert len(registry) == 0
