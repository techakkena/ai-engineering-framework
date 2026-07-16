"""Tests for ai_analytics.tracking.constants."""

from __future__ import annotations

from ai_analytics.tracking import constants


def test_default_values() -> None:
    assert constants.DEFAULT_TRACKING_NAME == "tracking"
    assert constants.DEFAULT_TRACKING_TYPE == "session"
    assert constants.DEFAULT_ENABLED is True


def test_supported_tracking_types() -> None:
    assert constants.SUPPORTED_TRACKING_TYPES == frozenset(
        {
            "session",
            "user",
            "request",
            "custom",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_TRACKING_NAME_LENGTH == 1
    assert constants.MAX_TRACKING_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.IDENTIFIER_KEY == "identifier"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.TAGS_KEY == "tags"
    assert constants.ENABLED_KEY == "enabled"