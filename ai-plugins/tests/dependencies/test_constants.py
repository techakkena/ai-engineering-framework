"""Tests for ai_plugins.dependencies.constants."""

from __future__ import annotations

from ai_plugins.dependencies import constants


def test_default_values() -> None:
    assert constants.DEFAULT_DEPENDENCY_NAME == "dependency"
    assert constants.DEFAULT_DEPENDENCY_TYPE == "required"
    assert constants.DEFAULT_ENABLED is True


def test_supported_dependency_types() -> None:
    assert constants.SUPPORTED_DEPENDENCY_TYPES == frozenset(
        {
            "required",
            "optional",
            "runtime",
            "development",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_DEPENDENCY_NAME_LENGTH == 1
    assert constants.MAX_DEPENDENCY_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.VERSION_KEY == "version"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"