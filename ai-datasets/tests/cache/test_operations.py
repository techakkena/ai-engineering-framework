"""
Unit tests for ai_datasets.cache.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.cache.exceptions import (
    CacheValidationError,
)
from ai_datasets.cache.operations import (
    CacheResult,
    cache_dataset,
    clear_cache,
    get_cache_statistics,
    get_cached_dataset,
    invalidate_cache,
)


def _dataset() -> list[dict[str, object]]:
    """Return a sample dataset."""
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]


def test_cache_dataset_success() -> None:
    """Caching a dataset should succeed."""
    result = cache_dataset(
        "customers",
        _dataset(),
    )

    assert isinstance(result, CacheResult)
    assert result.success is True
    assert result.task == "cache_dataset"


def test_cache_dataset_empty_key() -> None:
    """Empty cache keys should raise."""
    with pytest.raises(CacheValidationError):
        cache_dataset(
            "",
            _dataset(),
        )


def test_get_cached_dataset_success() -> None:
    """Getting a cached dataset should succeed."""
    result = get_cached_dataset("customers")

    assert result.success is True
    assert result.task == "get_cached_dataset"


def test_invalidate_cache_success() -> None:
    """Cache invalidation should succeed."""
    result = invalidate_cache("customers")

    assert result.success is True
    assert result.task == "invalidate_cache"


def test_clear_cache_success() -> None:
    """Cache clearing should succeed."""
    result = clear_cache()

    assert result.success is True
    assert result.task == "clear_cache"


def test_get_cache_statistics_success() -> None:
    """Getting cache statistics should succeed."""
    result = get_cache_statistics()

    assert result.success is True
    assert result.task == "get_cache_statistics"

    assert "entries" in result.data
    assert "hits" in result.data
    assert "misses" in result.data


@pytest.mark.parametrize(
    "operation",
    [
        get_cached_dataset,
        invalidate_cache,
    ],
)
def test_key_validation(
    operation,
) -> None:
    """All key-based operations should reject empty keys."""
    with pytest.raises(CacheValidationError):
        operation("")