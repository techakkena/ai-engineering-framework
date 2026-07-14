import pytest

from ai_evals.config.exceptions import (
    EvaluationConfigurationError,
)


def test_configuration_error() -> None:
    with pytest.raises(
        EvaluationConfigurationError,
    ):
        raise EvaluationConfigurationError()
