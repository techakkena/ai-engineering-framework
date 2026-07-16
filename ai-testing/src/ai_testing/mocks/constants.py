"""Constants for the ai_testing.mocks module."""

from __future__ import annotations

from typing import Final

DEFAULT_MOCK_NAME: Final[str] = "mock"

DEFAULT_ENABLED: Final[bool] = True
DEFAULT_RESET_AFTER_USE: Final[bool] = True

MIN_MOCK_NAME_LENGTH: Final[int] = 1
MAX_MOCK_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TARGET_KEY: Final[str] = "target"
VALUE_KEY: Final[str] = "value"
ENABLED_KEY: Final[str] = "enabled"
RESET_AFTER_USE_KEY: Final[str] = "reset_after_use"

__all__ = [
    "DEFAULT_ENABLED",
    "DEFAULT_MOCK_NAME",
    "DEFAULT_RESET_AFTER_USE",
    "ENABLED_KEY",
    "MAX_MOCK_NAME_LENGTH",
    "MIN_MOCK_NAME_LENGTH",
    "NAME_KEY",
    "RESET_AFTER_USE_KEY",
    "TARGET_KEY",
    "VALUE_KEY",
]