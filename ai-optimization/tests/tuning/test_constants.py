"""Tests for ai_optimization.tuning.constants."""

from __future__ import annotations

from ai_optimization.tuning import constants


def test_default_values() -> None:
    assert constants.DEFAULT_TUNING_NAME == "tuning"
    assert constants.DEFAULT_TUNING_STRATEGY == "grid"
    assert constants.DEFAULT_ENABLED is True


def test_supported_tuning_strategies() -> None:
    assert constants.SUPPORTED_TUNING_STRATEGIES == frozenset(
        {
            "grid",
            "random",
            "bayesian",
            "evolutionary",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_TUNING_NAME_LENGTH == 1
    assert constants.MAX_TUNING_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.STRATEGY_KEY == "strategy"
    assert constants.ITERATIONS_KEY == "iterations"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"