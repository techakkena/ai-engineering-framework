"""
Exceptions for the ai_datasets.cache package.
"""

from __future__ import annotations


class DatasetCacheError(Exception):
    """Base exception for dataset cache errors."""


class CacheValidationError(DatasetCacheError):
    """Raised when cache validation fails."""


class CacheKeyNotFoundError(DatasetCacheError):
    """Raised when a cache key cannot be found."""


class CacheWriteError(DatasetCacheError):
    """Raised when writing to the cache fails."""


class CacheReadError(DatasetCacheError):
    """Raised when reading from the cache fails."""


class CacheConfigurationError(DatasetCacheError):
    """Raised when the cache configuration is invalid."""


class CacheProviderError(DatasetCacheError):
    """Raised when an underlying cache provider fails."""