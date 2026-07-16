"""Tests for ai_cloud.monitoring.constants."""

from __future__ import annotations

from ai_cloud.monitoring import constants


def test_default_values() -> None:
    assert constants.DEFAULT_MONITOR_NAME == "monitor"
    assert constants.DEFAULT_MONITOR_TYPE == "metrics"
    assert constants.DEFAULT_ENABLED is True


def test_supported_monitor_types() -> None:
    assert constants.SUPPORTED_MONITOR_TYPES == frozenset(
        {
            "metrics",
            "logging",
            "tracing",
            "health",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_MONITOR_NAME_LENGTH == 1
    assert constants.MAX_MONITOR_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.INTERVAL_KEY == "interval"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"