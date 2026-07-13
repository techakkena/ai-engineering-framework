"""Constants for the ai_memory.store module."""

from __future__ import annotations

from enum import Enum


class StoreType(str, Enum):
    """Supported storage backends."""

    MEMORY = "memory"
    FILE = "file"
    SQLITE = "sqlite"
    REDIS = "redis"
    VECTOR = "vector"


class StoreState(str, Enum):
    """Store lifecycle states."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"


DEFAULT_STORE_NAME = "memory_store"
DEFAULT_STORE_NAMESPACE = "default"