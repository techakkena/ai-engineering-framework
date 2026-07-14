from ai_agents.utils.operations import (
    build_agent_name,
    validate_agent_name,
)


def test_build_agent_name() -> None:
    assert build_agent_name("Assistant") == "agent_assistant"


def test_build_agent_name_spaces() -> None:
    assert build_agent_name("My Agent") == "agent_my_agent"


def test_validate_agent_name_valid() -> None:
    assert validate_agent_name("agent_one")


def test_validate_agent_name_invalid() -> None:
    assert not validate_agent_name("")


def test_validate_agent_name_invalid_characters() -> None:
    assert not validate_agent_name("agent-one")
