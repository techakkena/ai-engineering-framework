"""Constants for the ai_optimization.profiling module."""

from __future__ import annotations

from typing import Final

# Default profiling configuration.
DEFAULT_PROFILE_NAME: Final[str] = "profile"
DEFAULT_PROFILE_TYPE: Final[str] = "cpu"
DEFAULT_ENABLED: Final[bool] = True

# Supported profiling types.
CPU_PROFILE: Final[str] = "cpu"
MEMORY_PROFILE: Final[str] = "memory"
IO_PROFILE: Final[str] = "io"
FULL_PROFILE: Final[str] = "full"

SUPPORTED_PROFILE_TYPES: Final[frozenset[str]] = frozenset(
    {
        CPU_PROFILE,
        MEMORY_PROFILE,
        IO_PROFILE,
        FULL_PROFILE,
    }
)

# Validation.
MIN_PROFILE_NAME_LENGTH: Final[int] = 1
MAX_PROFILE_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
INTERVAL_KEY: Final[str] = "interval"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "CPU_PROFILE",
    "DEFAULT_ENABLED",
    "DEFAULT_PROFILE_NAME",
    "DEFAULT_PROFILE_TYPE",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "FULL_PROFILE",
    "INTERVAL_KEY",
    "IO_PROFILE",
    "MAX_PROFILE_NAME_LENGTH",
    "MEMORY_PROFILE",
    "MIN_PROFILE_NAME_LENGTH",
    "NAME_KEY",
    "SUPPORTED_PROFILE_TYPES",
    "TYPE_KEY",
]