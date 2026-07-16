"""Constants for the ai_plugins.validation module."""

from __future__ import annotations

from typing import Final

# Default validation configuration.
DEFAULT_VALIDATION_NAME: Final[str] = "validation"
DEFAULT_VALIDATION_LEVEL: Final[str] = "standard"
DEFAULT_ENABLED: Final[bool] = True

# Supported validation levels.
BASIC_LEVEL: Final[str] = "basic"
STANDARD_LEVEL: Final[str] = "standard"
STRICT_LEVEL: Final[str] = "strict"
CUSTOM_LEVEL: Final[str] = "custom"

SUPPORTED_VALIDATION_LEVELS: Final[frozenset[str]] = frozenset(
    {
        BASIC_LEVEL,
        STANDARD_LEVEL,
        STRICT_LEVEL,
        CUSTOM_LEVEL,
    }
)

# Validation.
MIN_VALIDATION_NAME_LENGTH: Final[int] = 1
MAX_VALIDATION_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
LEVEL_KEY: Final[str] = "level"
RULE_COUNT_KEY: Final[str] = "rule_count"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "BASIC_LEVEL",
    "CUSTOM_LEVEL",
    "DEFAULT_ENABLED",
    "DEFAULT_VALIDATION_LEVEL",
    "DEFAULT_VALIDATION_NAME",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "LEVEL_KEY",
    "MAX_VALIDATION_NAME_LENGTH",
    "MIN_VALIDATION_NAME_LENGTH",
    "NAME_KEY",
    "RULE_COUNT_KEY",
    "STANDARD_LEVEL",
    "STRICT_LEVEL",
    "SUPPORTED_VALIDATION_LEVELS",
]