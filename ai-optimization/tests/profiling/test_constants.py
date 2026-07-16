"""Tests for ai_optimization.profiling.constants."""

from __future__ import annotations

from ai_optimization.profiling import constants


def test_default_values() -> None:
    assert constants.DEFAULT_PROFILE_NAME == "profile"
    assert constants.DEFAULT_PROFILE_TYPE == "cpu"
    assert constants.DEFAULT_ENABLED is True


def test_supported_profile_types() -> None:
    assert constants.SUPPORTED_PROFILE_TYPES == frozenset(
        {
            "cpu",
            "memory",
            "io",
            "full",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_PROFILE_NAME_LENGTH == 1
    assert constants.MAX_PROFILE_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.INTERVAL_KEY == "interval"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"