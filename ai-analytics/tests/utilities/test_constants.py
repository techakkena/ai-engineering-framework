"""Tests for ai_analytics.utilities.constants."""

from __future__ import annotations

from ai_analytics.utilities import constants


def test_default_values() -> None:
    assert constants.DEFAULT_NAME == "analytics"
    assert constants.DEFAULT_CATEGORY == "general"


def test_name_limits() -> None:
    assert constants.MIN_NAME_LENGTH == 1
    assert constants.MAX_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.CATEGORY_KEY == "category"
    assert constants.TAGS_KEY == "tags"