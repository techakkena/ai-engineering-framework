"""Constants for the ai_analytics.tracking module."""

from __future__ import annotations

from typing import Final

DEFAULT_TRACKING_NAME: Final[str] = "tracking"
DEFAULT_TRACKING_TYPE: Final[str] = "session"
DEFAULT_ENABLED: Final[bool] = True

SESSION_TRACKING: Final[str] = "session"
USER_TRACKING: Final[str] = "user"
REQUEST_TRACKING: Final[str] = "request"
CUSTOM_TRACKING: Final[str] = "custom"

SUPPORTED_TRACKING_TYPES: Final[frozenset[str]] = frozenset(
    {
        SESSION_TRACKING,
        USER_TRACKING,
        REQUEST_TRACKING,
        CUSTOM_TRACKING,
    }
)

MIN_TRACKING_NAME_LENGTH: Final[int] = 1
MAX_TRACKING_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
IDENTIFIER_KEY: Final[str] = "identifier"
DESCRIPTION_KEY: Final[str] = "description"
TAGS_KEY: Final[str] = "tags"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "CUSTOM_TRACKING",
    "DEFAULT_ENABLED",
    "DEFAULT_TRACKING_NAME",
    "DEFAULT_TRACKING_TYPE",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "IDENTIFIER_KEY",
    "MAX_TRACKING_NAME_LENGTH",
    "MIN_TRACKING_NAME_LENGTH",
    "NAME_KEY",
    "REQUEST_TRACKING",
    "SESSION_TRACKING",
    "SUPPORTED_TRACKING_TYPES",
    "TAGS_KEY",
    "TYPE_KEY",
    "USER_TRACKING",
]