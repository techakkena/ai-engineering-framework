"""Constants for the ai_docs.utilities module."""

from __future__ import annotations

from typing import Final

DEFAULT_VERSION: Final[str] = "1.0.0"
DEFAULT_AUTHOR: Final[str] = "Unknown"

MIN_NAME_LENGTH: Final[int] = 1
MAX_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
VERSION_KEY: Final[str] = "version"
AUTHOR_KEY: Final[str] = "author"
DESCRIPTION_KEY: Final[str] = "description"

__all__ = [
    "AUTHOR_KEY",
    "DEFAULT_AUTHOR",
    "DEFAULT_VERSION",
    "DESCRIPTION_KEY",
    "MAX_NAME_LENGTH",
    "MIN_NAME_LENGTH",
    "NAME_KEY",
    "VERSION_KEY",
]