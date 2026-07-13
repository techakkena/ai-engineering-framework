"""Tests for ai_memory.store.constants."""

from ai_memory.store.constants import (
    DEFAULT_STORE_NAME,
    DEFAULT_STORE_NAMESPACE,
    StoreState,
    StoreType,
)


def test_store_type_values() -> None:
    assert StoreType.MEMORY.value == "memory"
    assert StoreType.FILE.value == "file"
    assert StoreType.SQLITE.value == "sqlite"
    assert StoreType.REDIS.value == "redis"
    assert StoreType.VECTOR.value == "vector"


def test_store_state_values() -> None:
    assert StoreState.ACTIVE.value == "active"
    assert StoreState.INACTIVE.value == "inactive"
    assert StoreState.ARCHIVED.value == "archived"


def test_default_values() -> None:
    assert DEFAULT_STORE_NAME == "memory_store"
    assert DEFAULT_STORE_NAMESPACE == "default"