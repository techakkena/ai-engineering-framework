"""Constants for the ai_testing.snapshots module."""

from __future__ import annotations

from typing import Final

DEFAULT_SNAPSHOT_NAME: Final[str] = "snapshot"
DEFAULT_FORMAT: Final[str] = "json"
DEFAULT_ENABLED: Final[bool] = True

SUPPORTED_FORMATS: Final[frozenset[str]] = frozenset(
    {
        "json",
        "yaml",
        "text",
    }
)

MIN_SNAPSHOT_NAME_LENGTH: Final[int] = 1
MAX_SNAPSHOT_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
FORMAT_KEY: Final[str] = "format"
CONTENT_KEY: Final[str] = "content"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "CONTENT_KEY",
    "DEFAULT_ENABLED",
    "DEFAULT_FORMAT",
    "DEFAULT_SNAPSHOT_NAME",
    "ENABLED_KEY",
    "FORMAT_KEY",
    "MAX_SNAPSHOT_NAME_LENGTH",
    "MIN_SNAPSHOT_NAME_LENGTH",
    "NAME_KEY",
    "SUPPORTED_FORMATS",
]