from ai_evals.config.constants import (
    DEFAULT_ENABLED,
    DEFAULT_METRIC,
    DEFAULT_PASS_THRESHOLD,
    DEFAULT_SAVE_REPORTS,
)


def test_defaults() -> None:
    assert DEFAULT_ENABLED is True
    assert DEFAULT_METRIC == "overall"
    assert DEFAULT_PASS_THRESHOLD == 0.80
    assert DEFAULT_SAVE_REPORTS is True
