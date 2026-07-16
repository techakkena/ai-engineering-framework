"""Exceptions for the ai_optimization.caching module."""

from __future__ import annotations


class CacheError(Exception):
    """Base exception for cache operations."""


class CacheValidationError(CacheError):
    """Raised when cache validation fails."""


class CacheRegistrationError(CacheError):
    """Raised when cache registration fails."""


class CacheNotFoundError(CacheRegistrationError):
    """Raised when a requested cache cannot be found."""


class DuplicateCacheError(CacheRegistrationError):
    """Raised when attempting to register a duplicate cache."""


class UnsupportedCacheBackendError(CacheValidationError):
    """Raised when an unsupported cache backend is specified."""


__all__ = [
    "CacheError",
    "CacheNotFoundError",
    "CacheRegistrationError",
    "CacheValidationError",
    "DuplicateCacheError",
    "UnsupportedCacheBackendError",
]