from ai_evals.metrics.constants import (
    DEFAULT_METRIC_NAME,
)


def test_default_metric_name() -> None:
    assert DEFAULT_METRIC_NAME == "score"
