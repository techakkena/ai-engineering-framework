from ai_evals.base.constants import (
    EvaluationStatus,
)
from ai_evals.base.operations import (
    BaseEvaluator,
    EvaluationContext,
    EvaluationResult,
)


class DummyEvaluator(BaseEvaluator):
    def evaluate(
        self,
        context: EvaluationContext,
    ) -> EvaluationResult:
        return EvaluationResult(
            score=1.0,
            status=EvaluationStatus.PASSED,
        )


def test_result_defaults() -> None:
    result = EvaluationResult()

    assert result.score == 0.0
    assert result.status is EvaluationStatus.PENDING
    assert result.metadata == {}


def test_context_defaults() -> None:
    context = EvaluationContext()

    assert context.inputs == {}
    assert context.outputs == {}


def test_dummy_evaluator() -> None:
    evaluator = DummyEvaluator()

    result = evaluator.evaluate(
        EvaluationContext(),
    )

    assert result.score == 1.0
    assert result.status is EvaluationStatus.PASSED
