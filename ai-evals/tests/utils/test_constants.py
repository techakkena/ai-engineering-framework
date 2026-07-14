from ai_evals.utils.constants import (
    DEFAULT_EVALUATION_PREFIX,
)


def test_default_evaluation_prefix() -> None:
    assert DEFAULT_EVALUATION_PREFIX == "evaluation"
