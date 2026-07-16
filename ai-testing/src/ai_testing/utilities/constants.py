"""Constants for the ai_testing.utilities module."""

from __future__ import annotations

from typing import Final

DEFAULT_TEST_NAME: Final[str] = "test"

DEFAULT_CATEGORY: Final[str] = "general"

MIN_NAME_LENGTH: Final[int] = 1
MAX_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
CATEGORY_KEY: Final[str] = "category"
TAGS_KEY: Final[str] = "tags"

__all__ = [
    "CATEGORY_KEY",
    "DEFAULT_CATEGORY",
    "DEFAULT_TEST_NAME",
    "MAX_NAME_LENGTH",
    "MIN_NAME_LENGTH",
    "NAME_KEY",
    "TAGS_KEY",
]