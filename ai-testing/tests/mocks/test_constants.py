"""Tests for ai_testing.mocks.constants."""

from __future__ import annotations

from ai_testing.mocks import constants


def test_default_mock_name() -> None:
    assert constants.DEFAULT_MOCK_NAME == "mock"


def test_default_flags() -> None:
    assert constants.DEFAULT_ENABLED is True
    assert constants.DEFAULT_RESET_AFTER_USE is True


def test_name_limits() -> None:
    assert constants.MIN_MOCK_NAME_LENGTH == 1
    assert constants.MAX_MOCK_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TARGET_KEY == "target"
    assert constants.VALUE_KEY == "value"
    assert constants.ENABLED_KEY == "enabled"
    assert constants.RESET_AFTER_USE_KEY == "reset_after_use"