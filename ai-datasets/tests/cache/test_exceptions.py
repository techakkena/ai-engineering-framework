"""
Unit tests for ai_datasets.cache.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.cache.exceptions import (
    CacheConfigurationError,
    CacheKeyNotFoundError,
    CacheProviderError,
    CacheReadError,
    CacheValidationError,
    CacheWriteError,
    DatasetCacheError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        CacheValidationError,
        CacheKeyNotFoundError,
        CacheWriteError,
        CacheReadError,
        CacheConfigurationError,
        CacheProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetCacheError],
) -> None:
    """Every custom exception should inherit from DatasetCacheError."""
    assert issubclass(
        exception_class,
        DatasetCacheError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetCacheError,
        match="cache failure",
    ):
        raise DatasetCacheError(
            "cache failure",
        )