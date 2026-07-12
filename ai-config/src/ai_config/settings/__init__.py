"""
Settings module.

Author: TECHAKKENA
"""

from ai_config.settings.constants import (
    DEFAULT_COPY_ON_MERGE,
    DEFAULT_SEPARATOR,
    DEFAULT_SETTINGS,
)
from ai_config.settings.exceptions import (
    InvalidSettingError,
    SettingNotFoundError,
    SettingsError,
)
from ai_config.settings.operations import Settings

__all__ = [
    "DEFAULT_SETTINGS",
    "DEFAULT_SEPARATOR",
    "DEFAULT_COPY_ON_MERGE",
    "Settings",
    "SettingsError",
    "SettingNotFoundError",
    "InvalidSettingError",
]
