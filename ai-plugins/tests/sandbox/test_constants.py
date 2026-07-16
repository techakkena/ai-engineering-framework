"""Tests for ai_plugins.sandbox.constants."""

from __future__ import annotations

from ai_plugins.sandbox import constants


def test_default_values() -> None:
    assert constants.DEFAULT_SANDBOX_NAME == "sandbox"
    assert constants.DEFAULT_SANDBOX_MODE == "isolated"
    assert constants.DEFAULT_ENABLED is True


def test_supported_sandbox_modes() -> None:
    assert constants.SUPPORTED_SANDBOX_MODES == frozenset(
        {
            "isolated",
            "process",
            "container",
            "virtual_machine",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_SANDBOX_NAME_LENGTH == 1
    assert constants.MAX_SANDBOX_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.MODE_KEY == "mode"
    assert constants.MEMORY_LIMIT_KEY == "memory_limit"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"