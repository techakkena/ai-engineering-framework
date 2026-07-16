"""Constants for the ai_enterprise.auditing module."""

from __future__ import annotations

from typing import Final

DEFAULT_AUDIT_NAME: Final[str] = "audit"
DEFAULT_AUDIT_LEVEL: Final[str] = "info"
DEFAULT_ENABLED: Final[bool] = True

INFO_LEVEL: Final[str] = "info"
WARNING_LEVEL: Final[str] = "warning"
ERROR_LEVEL: Final[str] = "error"
CRITICAL_LEVEL: Final[str] = "critical"

SUPPORTED_AUDIT_LEVELS: Final[frozenset[str]] = frozenset(
    {
        INFO_LEVEL,
        WARNING_LEVEL,
        ERROR_LEVEL,
        CRITICAL_LEVEL,
    }
)

MIN_AUDIT_NAME_LENGTH: Final[int] = 3
MAX_AUDIT_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
LEVEL_KEY: Final[str] = "level"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "CRITICAL_LEVEL",
    "DEFAULT_AUDIT_LEVEL",
    "DEFAULT_AUDIT_NAME",
    "DEFAULT_ENABLED",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "ERROR_LEVEL",
    "INFO_LEVEL",
    "LEVEL_KEY",
    "MAX_AUDIT_NAME_LENGTH",
    "MIN_AUDIT_NAME_LENGTH",
    "NAME_KEY",
    "SUPPORTED_AUDIT_LEVELS",
    "WARNING_LEVEL",
]