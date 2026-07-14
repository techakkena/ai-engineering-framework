import pytest

from ai_evals.scoring.exceptions import (
    ScoringError,
)


def test_scoring_error() -> None:
    with pytest.raises(
        ScoringError,
    ):
        raise ScoringError()
