import pytest

from ai_workflows.conditions.exceptions import (
    ConditionEvaluationError,
)


def test_condition_evaluation_error() -> None:
    with pytest.raises(
        ConditionEvaluationError,
    ):
        raise ConditionEvaluationError()
