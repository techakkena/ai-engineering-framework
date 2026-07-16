"""Tests for ai_plugins.validation.constants."""

from __future__ import annotations

from ai_plugins.validation import constants


def test_default_values() -> None:
    assert constants.DEFAULT_VALIDATION_NAME == "validation"
    assert constants.DEFAULT_VALIDATION_LEVEL == "standard"
    assert constants.DEFAULT_ENABLED is True


def test_supported_validation_levels() -> None:
    assert constants.SUPPORTED_VALIDATION_LEVELS == frozenset(
        {
            "basic",
            "standard",
            "strict",
            "custom",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_VALIDATION_NAME_LENGTH == 1
    assert constants.MAX_VALIDATION_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.LEVEL_KEY == "level"
    assert constants.RULE_COUNT_KEY == "rule_count"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"