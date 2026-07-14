from ai_evals.base.operations import (
    EvaluationContext,
)

from ai_evals.evaluators.operations import (
    Evaluator,
    EvaluatorRegistry,
)


def test_default_evaluator() -> None:
    evaluator = Evaluator()

    result = evaluator.evaluate(
        EvaluationContext(),
    )

    assert result.score == 1.0


def test_custom_score() -> None:
    evaluator = Evaluator(
        score=0.75,
    )

    result = evaluator.evaluate(
        EvaluationContext(),
    )

    assert result.score == 0.75


def test_registry() -> None:
    registry = EvaluatorRegistry()

    evaluator = Evaluator(
        name="rag",
    )

    registry.register(
        evaluator,
    )

    assert registry.count == 1

    assert registry.get("rag") is evaluator


def test_missing_evaluator() -> None:
    registry = EvaluatorRegistry()

    assert registry.get("missing") is None
