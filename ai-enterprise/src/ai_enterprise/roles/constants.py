"""Constants for the ai_enterprise.roles module."""

from __future__ import annotations

from typing import Final

DEFAULT_ROLE_NAME: Final[str] = "user"
DEFAULT_ENABLED: Final[bool] = True

ADMIN_ROLE: Final[str] = "admin"
MANAGER_ROLE: Final[str] = "manager"
USER_ROLE: Final[str] = "user"
VIEWER_ROLE: Final[str] = "viewer"

SUPPORTED_ROLE_NAMES: Final[frozenset[str]] = frozenset(
    {
        ADMIN_ROLE,
        MANAGER_ROLE,
        USER_ROLE,
        VIEWER_ROLE,
    }
)

MIN_ROLE_NAME_LENGTH: Final[int] = 3
MAX_ROLE_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
DESCRIPTION_KEY: Final[str] = "description"
PERMISSIONS_KEY: Final[str] = "permissions"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "ADMIN_ROLE",
    "DEFAULT_ENABLED",
    "DEFAULT_ROLE_NAME",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "MANAGER_ROLE",
    "MAX_ROLE_NAME_LENGTH",
    "MIN_ROLE_NAME_LENGTH",
    "NAME_KEY",
    "PERMISSIONS_KEY",
    "SUPPORTED_ROLE_NAMES",
    "USER_ROLE",
    "VIEWER_ROLE",
]