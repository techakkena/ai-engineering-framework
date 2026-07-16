"""Constants for the ai_plugins.dependencies module."""

from __future__ import annotations

from typing import Final

# Default dependency configuration.
DEFAULT_DEPENDENCY_NAME: Final[str] = "dependency"
DEFAULT_DEPENDENCY_TYPE: Final[str] = "required"
DEFAULT_ENABLED: Final[bool] = True

# Supported dependency types.
REQUIRED_TYPE: Final[str] = "required"
OPTIONAL_TYPE: Final[str] = "optional"
RUNTIME_TYPE: Final[str] = "runtime"
DEVELOPMENT_TYPE: Final[str] = "development"

SUPPORTED_DEPENDENCY_TYPES: Final[frozenset[str]] = frozenset(
    {
        REQUIRED_TYPE,
        OPTIONAL_TYPE,
        RUNTIME_TYPE,
        DEVELOPMENT_TYPE,
    }
)

# Validation.
MIN_DEPENDENCY_NAME_LENGTH: Final[int] = 1
MAX_DEPENDENCY_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
VERSION_KEY: Final[str] = "version"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_DEPENDENCY_NAME",
    "DEFAULT_DEPENDENCY_TYPE",
    "DEFAULT_ENABLED",
    "DEVELOPMENT_TYPE",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "MAX_DEPENDENCY_NAME_LENGTH",
    "MIN_DEPENDENCY_NAME_LENGTH",
    "NAME_KEY",
    "OPTIONAL_TYPE",
    "REQUIRED_TYPE",
    "RUNTIME_TYPE",
    "SUPPORTED_DEPENDENCY_TYPES",
    "TYPE_KEY",
    "VERSION_KEY",
]