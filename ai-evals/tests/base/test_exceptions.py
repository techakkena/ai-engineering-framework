import pytest

from ai_evals.base.exceptions import (
    EvaluationConfigurationError,
    EvaluationError,
)


def test_evaluation_error() -> None:
    with pytest.raises(EvaluationError):
        raise EvaluationError()


def test_configuration_error() -> None:
    with pytest.raises(
        EvaluationConfigurationError,
    ):
        raise EvaluationConfigurationError()
