"""Constants for the ai_cloud.storage module."""

from __future__ import annotations

from typing import Final

DEFAULT_STORAGE_NAME: Final[str] = "storage"
DEFAULT_STORAGE_TYPE: Final[str] = "object"
DEFAULT_ENABLED: Final[bool] = True

OBJECT_STORAGE: Final[str] = "object"
BLOCK_STORAGE: Final[str] = "block"
FILE_STORAGE: Final[str] = "file"
ARCHIVE_STORAGE: Final[str] = "archive"

SUPPORTED_STORAGE_TYPES: Final[frozenset[str]] = frozenset(
    {
        OBJECT_STORAGE,
        BLOCK_STORAGE,
        FILE_STORAGE,
        ARCHIVE_STORAGE,
    }
)

MIN_STORAGE_NAME_LENGTH: Final[int] = 1
MAX_STORAGE_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
CAPACITY_KEY: Final[str] = "capacity"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "ARCHIVE_STORAGE",
    "BLOCK_STORAGE",
    "CAPACITY_KEY",
    "DEFAULT_ENABLED",
    "DEFAULT_STORAGE_NAME",
    "DEFAULT_STORAGE_TYPE",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "FILE_STORAGE",
    "MAX_STORAGE_NAME_LENGTH",
    "MIN_STORAGE_NAME_LENGTH",
    "NAME_KEY",
    "OBJECT_STORAGE",
    "SUPPORTED_STORAGE_TYPES",
    "TYPE_KEY",
]