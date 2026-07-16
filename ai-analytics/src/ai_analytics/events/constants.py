"""Constants for the ai_analytics.events module."""

from __future__ import annotations

from typing import Final

# Default event configuration.
DEFAULT_EVENT_NAME: Final[str] = "event"
DEFAULT_EVENT_TYPE: Final[str] = "custom"
DEFAULT_ENABLED: Final[bool] = True

# Supported event types.
CUSTOM_EVENT: Final[str] = "custom"
SYSTEM_EVENT: Final[str] = "system"
USER_EVENT: Final[str] = "user"
APPLICATION_EVENT: Final[str] = "application"

SUPPORTED_EVENT_TYPES: Final[frozenset[str]] = frozenset(
    {
        CUSTOM_EVENT,
        SYSTEM_EVENT,
        USER_EVENT,
        APPLICATION_EVENT,
    }
)

# Validation.
MIN_EVENT_NAME_LENGTH: Final[int] = 1
MAX_EVENT_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
PAYLOAD_KEY: Final[str] = "payload"
DESCRIPTION_KEY: Final[str] = "description"
TAGS_KEY: Final[str] = "tags"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "APPLICATION_EVENT",
    "CUSTOM_EVENT",
    "DEFAULT_ENABLED",
    "DEFAULT_EVENT_NAME",
    "DEFAULT_EVENT_TYPE",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "MAX_EVENT_NAME_LENGTH",
    "MIN_EVENT_NAME_LENGTH",
    "NAME_KEY",
    "PAYLOAD_KEY",
    "SUPPORTED_EVENT_TYPES",
    "SYSTEM_EVENT",
    "TAGS_KEY",
    "TYPE_KEY",
    "USER_EVENT",
]