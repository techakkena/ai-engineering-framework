"""Constants for the ai_optimization.caching module."""

from __future__ import annotations

from typing import Final

# Default cache configuration.
DEFAULT_CACHE_NAME: Final[str] = "cache"
DEFAULT_CACHE_BACKEND: Final[str] = "memory"
DEFAULT_ENABLED: Final[bool] = True

# Supported cache backends.
MEMORY_BACKEND: Final[str] = "memory"
REDIS_BACKEND: Final[str] = "redis"
DISK_BACKEND: Final[str] = "disk"
HYBRID_BACKEND: Final[str] = "hybrid"

SUPPORTED_CACHE_BACKENDS: Final[frozenset[str]] = frozenset(
    {
        MEMORY_BACKEND,
        REDIS_BACKEND,
        DISK_BACKEND,
        HYBRID_BACKEND,
    }
)

# Validation.
MIN_CACHE_NAME_LENGTH: Final[int] = 1
MAX_CACHE_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
BACKEND_KEY: Final[str] = "backend"
CAPACITY_KEY: Final[str] = "capacity"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "BACKEND_KEY",
    "CAPACITY_KEY",
    "DEFAULT_CACHE_BACKEND",
    "DEFAULT_CACHE_NAME",
    "DEFAULT_ENABLED",
    "DESCRIPTION_KEY",
    "DISK_BACKEND",
    "ENABLED_KEY",
    "HYBRID_BACKEND",
    "MAX_CACHE_NAME_LENGTH",
    "MEMORY_BACKEND",
    "MIN_CACHE_NAME_LENGTH",
    "NAME_KEY",
    "REDIS_BACKEND",
    "SUPPORTED_CACHE_BACKENDS",
]