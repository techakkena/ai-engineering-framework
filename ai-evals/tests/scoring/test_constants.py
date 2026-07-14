from ai_evals.scoring.constants import (
    DEFAULT_SCORE_NAME,
)


def test_default_score_name() -> None:
    assert DEFAULT_SCORE_NAME == "overall"
