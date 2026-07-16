"""Tests for ai_analytics.aggregation.constants."""

from __future__ import annotations

from ai_analytics.aggregation import constants


def test_default_values() -> None:
    assert constants.DEFAULT_AGGREGATION_NAME == "aggregation"
    assert constants.DEFAULT_AGGREGATION_TYPE == "sum"
    assert constants.DEFAULT_ENABLED is True


def test_supported_aggregation_types() -> None:
    assert constants.SUPPORTED_AGGREGATION_TYPES == frozenset(
        {
            "sum",
            "average",
            "min",
            "max",
            "count",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_AGGREGATION_NAME_LENGTH == 1
    assert constants.MAX_AGGREGATION_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.FIELD_KEY == "field"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"