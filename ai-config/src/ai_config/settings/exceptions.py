"""
Custom exceptions for the settings module.

Author: TECHAKKENA
"""


class SettingsError(Exception):
    """Base exception for settings operations."""


class SettingNotFoundError(SettingsError):
    """Raised when a setting key cannot be found."""


class InvalidSettingError(SettingsError):
    """Raised when invalid settings are provided."""
