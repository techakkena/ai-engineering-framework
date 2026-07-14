import pytest

from ai_evals.experiments.exceptions import (
    ExperimentError,
)


def test_experiment_error() -> None:
    with pytest.raises(
        ExperimentError,
    ):
        raise ExperimentError()
