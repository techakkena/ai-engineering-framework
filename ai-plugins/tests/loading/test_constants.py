"""Tests for ai_plugins.loading.constants."""

from __future__ import annotations

from ai_plugins.loading import constants


def test_default_values() -> None:
    assert constants.DEFAULT_LOADER_NAME == "loader"
    assert constants.DEFAULT_LOADING_MODE == "lazy"
    assert constants.DEFAULT_ENABLED is True


def test_supported_loading_modes() -> None:
    assert constants.SUPPORTED_LOADING_MODES == frozenset(
        {
            "lazy",
            "eager",
            "on_demand",
            "isolated",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_LOADER_NAME_LENGTH == 1
    assert constants.MAX_LOADER_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.MODE_KEY == "mode"
    assert constants.TIMEOUT_KEY == "timeout"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"