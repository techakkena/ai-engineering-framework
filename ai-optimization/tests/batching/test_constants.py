"""Tests for ai_optimization.batching.constants."""

from __future__ import annotations

from ai_optimization.batching import constants


def test_default_values() -> None:
    assert constants.DEFAULT_BATCH_NAME == "batch"
    assert constants.DEFAULT_BATCH_STRATEGY == "fixed"
    assert constants.DEFAULT_ENABLED is True


def test_supported_batch_strategies() -> None:
    assert constants.SUPPORTED_BATCH_STRATEGIES == frozenset(
        {
            "fixed",
            "dynamic",
            "adaptive",
            "streaming",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_BATCH_NAME_LENGTH == 1
    assert constants.MAX_BATCH_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.STRATEGY_KEY == "strategy"
    assert constants.SIZE_KEY == "size"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"