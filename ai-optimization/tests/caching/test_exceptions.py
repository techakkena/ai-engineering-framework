"""Tests for ai_optimization.caching.exceptions."""

from __future__ import annotations

import pytest

from ai_optimization.caching.exceptions import (
    CacheError,
    CacheNotFoundError,
    CacheRegistrationError,
    CacheValidationError,
    DuplicateCacheError,
    UnsupportedCacheBackendError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(CacheValidationError, CacheError)
    assert issubclass(CacheRegistrationError, CacheError)
    assert issubclass(
        CacheNotFoundError,
        CacheRegistrationError,
    )
    assert issubclass(
        DuplicateCacheError,
        CacheRegistrationError,
    )
    assert issubclass(
        UnsupportedCacheBackendError,
        CacheValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (CacheError, "base"),
        (CacheValidationError, "validation"),
        (CacheRegistrationError, "registration"),
        (CacheNotFoundError, "missing"),
        (DuplicateCacheError, "duplicate"),
        (UnsupportedCacheBackendError, "backend"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)