"""Constants for the ai_enterprise.permissions module."""

from __future__ import annotations

from typing import Final

DEFAULT_PERMISSION_NAME: Final[str] = "read"
DEFAULT_RESOURCE: Final[str] = "resource"
DEFAULT_ENABLED: Final[bool] = True

READ_PERMISSION: Final[str] = "read"
WRITE_PERMISSION: Final[str] = "write"
UPDATE_PERMISSION: Final[str] = "update"
DELETE_PERMISSION: Final[str] = "delete"
ADMIN_PERMISSION: Final[str] = "admin"

SUPPORTED_PERMISSION_NAMES: Final[frozenset[str]] = frozenset(
    {
        READ_PERMISSION,
        WRITE_PERMISSION,
        UPDATE_PERMISSION,
        DELETE_PERMISSION,
        ADMIN_PERMISSION,
    }
)

MIN_PERMISSION_NAME_LENGTH: Final[int] = 4
MAX_PERMISSION_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
RESOURCE_KEY: Final[str] = "resource"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "ADMIN_PERMISSION",
    "DEFAULT_ENABLED",
    "DEFAULT_PERMISSION_NAME",
    "DEFAULT_RESOURCE",
    "DELETE_PERMISSION",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "MAX_PERMISSION_NAME_LENGTH",
    "MIN_PERMISSION_NAME_LENGTH",
    "NAME_KEY",
    "READ_PERMISSION",
    "RESOURCE_KEY",
    "SUPPORTED_PERMISSION_NAMES",
    "UPDATE_PERMISSION",
    "WRITE_PERMISSION",
]