from ai_evals.evaluators.constants import (
    DEFAULT_EVALUATOR_NAME,
)


def test_default_name() -> None:
    assert DEFAULT_EVALUATOR_NAME == "default"
