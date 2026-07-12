"""
Tests for settings exceptions.
"""

from ai_config.settings.exceptions import (
    InvalidSettingError,
    SettingNotFoundError,
    SettingsError,
)


def test_settings_error() -> None:
    exception = SettingsError("error")

    assert isinstance(exception, Exception)


def test_setting_not_found_error() -> None:
    exception = SettingNotFoundError("missing")

    assert isinstance(exception, SettingsError)


def test_invalid_setting_error() -> None:
    exception = InvalidSettingError("invalid")

    assert isinstance(exception, SettingsError)
