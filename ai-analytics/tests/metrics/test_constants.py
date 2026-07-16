"""Tests for ai_analytics.metrics.constants."""

from __future__ import annotations

from ai_analytics.metrics import constants


def test_default_values() -> None:
    assert constants.DEFAULT_METRIC_NAME == "metric"
    assert constants.DEFAULT_METRIC_TYPE == "counter"
    assert constants.DEFAULT_ENABLED is True


def test_supported_metric_types() -> None:
    assert constants.SUPPORTED_METRIC_TYPES == frozenset(
        {
            "counter",
            "gauge",
            "histogram",
            "summary",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_METRIC_NAME_LENGTH == 1
    assert constants.MAX_METRIC_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.VALUE_KEY == "value"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.TAGS_KEY == "tags"
    assert constants.ENABLED_KEY == "enabled"