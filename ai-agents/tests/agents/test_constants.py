from ai_agents.agents.constants import (
    DEFAULT_AGENT_DESCRIPTION,
    DEFAULT_AGENT_NAME,
)


def test_default_name() -> None:
    assert DEFAULT_AGENT_NAME == "agent"


def test_default_description() -> None:
    assert "Default" in DEFAULT_AGENT_DESCRIPTION
