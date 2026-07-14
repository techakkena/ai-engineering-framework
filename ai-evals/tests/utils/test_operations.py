from ai_evals.utils.operations import (
    build_evaluation_name,
    validate_evaluation_name,
)


def test_build_evaluation_name() -> None:
    assert build_evaluation_name("RAG Benchmark") == "evaluation_rag_benchmark"


def test_build_evaluation_name_trim() -> None:
    assert (
        build_evaluation_name("  Agent Evaluation  ") == "evaluation_agent_evaluation"
    )


def test_validate_evaluation_name() -> None:
    assert validate_evaluation_name("evaluation_accuracy")


def test_validate_empty_name() -> None:
    assert not validate_evaluation_name("")


def test_validate_invalid_name() -> None:
    assert not validate_evaluation_name("evaluation-accuracy")
