from ai_observability.utils.operations import (
    build_observation_name,
    validate_observation_name,
)


def test_build_observation_name() -> None:
    assert build_observation_name("LLM Call") == "observation_llm_call"


def test_build_observation_name_trim() -> None:
    assert build_observation_name("  Agent Run  ") == "observation_agent_run"


def test_validate_observation_name() -> None:
    assert validate_observation_name("observation_trace")


def test_validate_empty_name() -> None:
    assert not validate_observation_name("")


def test_validate_invalid_name() -> None:
    assert not validate_observation_name("observation-trace")
