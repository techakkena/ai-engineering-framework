import pytest

from ai_evals.config.operations import (
    EvaluationConfig,
)


def test_default_config() -> None:
    config = EvaluationConfig()

    assert config.enabled is True
    assert config.default_metric == "overall"
    assert config.pass_threshold == 0.80
    assert config.save_reports is True


def test_validate_success() -> None:
    EvaluationConfig().validate()


def test_invalid_metric() -> None:
    config = EvaluationConfig(
        default_metric="",
    )

    with pytest.raises(ValueError):
        config.validate()


def test_invalid_threshold() -> None:
    config = EvaluationConfig(
        pass_threshold=2.0,
    )

    with pytest.raises(ValueError):
        config.validate()
