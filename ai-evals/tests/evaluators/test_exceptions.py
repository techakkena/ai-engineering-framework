import pytest

from ai_evals.evaluators.exceptions import (
    EvaluatorError,
)


def test_evaluator_error() -> None:
    with pytest.raises(EvaluatorError):
        raise EvaluatorError()
