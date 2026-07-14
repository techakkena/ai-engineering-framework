from ai_evals.base.constants import (
    EvaluationStatus,
)


def test_status_values() -> None:
    assert EvaluationStatus.PENDING.value == "pending"
    assert EvaluationStatus.RUNNING.value == "running"
    assert EvaluationStatus.PASSED.value == "passed"
    assert EvaluationStatus.FAILED.value == "failed"


def test_status_count() -> None:
    assert len(EvaluationStatus) == 4
