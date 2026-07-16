"""Constants for the ai_enterprise.users module."""

from __future__ import annotations

from typing import Final

DEFAULT_USER_ROLE: Final[str] = "user"
DEFAULT_ENABLED: Final[bool] = True

ADMIN_ROLE: Final[str] = "admin"
MANAGER_ROLE: Final[str] = "manager"
USER_ROLE: Final[str] = "user"
VIEWER_ROLE: Final[str] = "viewer"

SUPPORTED_USER_ROLES: Final[frozenset[str]] = frozenset(
    {
        ADMIN_ROLE,
        MANAGER_ROLE,
        USER_ROLE,
        VIEWER_ROLE,
    }
)

MIN_USERNAME_LENGTH: Final[int] = 3
MAX_USERNAME_LENGTH: Final[int] = 255

USERNAME_KEY: Final[str] = "username"
EMAIL_KEY: Final[str] = "email"
ROLE_KEY: Final[str] = "role"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "ADMIN_ROLE",
    "DEFAULT_ENABLED",
    "DEFAULT_USER_ROLE",
    "EMAIL_KEY",
    "ENABLED_KEY",
    "MANAGER_ROLE",
    "MAX_USERNAME_LENGTH",
    "MIN_USERNAME_LENGTH",
    "ROLE_KEY",
    "SUPPORTED_USER_ROLES",
    "USERNAME_KEY",
    "USER_ROLE",
    "VIEWER_ROLE",
]