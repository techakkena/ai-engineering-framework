"""Constants for the ai_testing.pytest module."""

from __future__ import annotations

from typing import Final

DEFAULT_TEST_PATH: Final[str] = "tests"
DEFAULT_VERBOSE: Final[bool] = False
DEFAULT_FAIL_FAST: Final[bool] = False

MIN_CONFIGURATION_NAME_LENGTH: Final[int] = 1
MAX_CONFIGURATION_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TEST_PATH_KEY: Final[str] = "test_path"
VERBOSE_KEY: Final[str] = "verbose"
FAIL_FAST_KEY: Final[str] = "fail_fast"

__all__ = [
    "DEFAULT_FAIL_FAST",
    "DEFAULT_TEST_PATH",
    "DEFAULT_VERBOSE",
    "FAIL_FAST_KEY",
    "MAX_CONFIGURATION_NAME_LENGTH",
    "MIN_CONFIGURATION_NAME_LENGTH",
    "NAME_KEY",
    "TEST_PATH_KEY",
    "VERBOSE_KEY",
]