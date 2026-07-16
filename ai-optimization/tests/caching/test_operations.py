"""Tests for ai_optimization.caching.operations."""

from __future__ import annotations

import pytest

from ai_optimization.caching.constants import (
    DEFAULT_CACHE_BACKEND,
    DEFAULT_ENABLED,
)
from ai_optimization.caching.exceptions import (
    CacheNotFoundError,
    CacheValidationError,
    DuplicateCacheError,
    UnsupportedCacheBackendError,
)
from ai_optimization.caching.operations import (
    CacheDefinition,
    CacheRegistry,
    build_cache,
)


def test_cache_definition_defaults() -> None:
    cache = CacheDefinition(
        name="default",
        capacity=100,
    )

    assert cache.name == "default"
    assert cache.capacity == 100
    assert cache.backend == DEFAULT_CACHE_BACKEND
    assert cache.description == ""
    assert cache.enabled is DEFAULT_ENABLED


def test_cache_definition_trims_name() -> None:
    cache = CacheDefinition(
        name="  default  ",
        capacity=100,
    )

    assert cache.name == "default"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(CacheValidationError):
        CacheDefinition(
            name=name,
            capacity=100,
        )


@pytest.mark.parametrize(
    "capacity",
    [
        0,
        -1,
        -100,
    ],
)
def test_invalid_capacity(
    capacity: int,
) -> None:
    with pytest.raises(CacheValidationError):
        CacheDefinition(
            name="cache",
            capacity=capacity,
        )


def test_invalid_backend() -> None:
    with pytest.raises(
        UnsupportedCacheBackendError,
    ):
        CacheDefinition(
            name="cache",
            capacity=100,
            backend="sqlite",
        )


def test_build_cache() -> None:
    cache = build_cache(
        name="redis",
        capacity=500,
        backend="redis",
        description="Redis cache",
    )

    assert cache.name == "redis"
    assert cache.capacity == 500
    assert cache.backend == "redis"
    assert cache.description == "Redis cache"


def test_registry_register_and_get() -> None:
    registry = CacheRegistry()

    cache = build_cache(
        name="default",
        capacity=100,
    )

    registry.register(cache)

    assert registry.get("default") is cache
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = CacheRegistry()

    cache = build_cache(
        name="default",
        capacity=100,
    )

    registry.register(cache)

    with pytest.raises(DuplicateCacheError):
        registry.register(cache)


def test_registry_unregister() -> None:
    registry = CacheRegistry()

    cache = build_cache(
        name="default",
        capacity=100,
    )

    registry.register(cache)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = CacheRegistry()

    with pytest.raises(CacheNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = CacheRegistry()

    with pytest.raises(CacheNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = CacheRegistry()

    registry.register(
        build_cache(
            name="one",
            capacity=1,
        )
    )
    registry.register(
        build_cache(
            name="two",
            capacity=2,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = CacheRegistry()

    first = build_cache(
        name="one",
        capacity=1,
    )
    second = build_cache(
        name="two",
        capacity=2,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = CacheRegistry()

    assert 123 not in registry