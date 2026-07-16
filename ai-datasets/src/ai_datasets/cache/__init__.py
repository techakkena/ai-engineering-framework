"""
ai_datasets.cache

Enterprise dataset cache module for the AI Engineering Framework.

This package provides provider-independent dataset caching capabilities,
including storing, retrieving, invalidating, clearing, and cache statistics.

Modules
-------
constants
    Cache-specific constants.

exceptions
    Cache-specific exception hierarchy.

operations
    High-level dataset cache operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_datasets.cache.operations import (
    cache_dataset,
    clear_cache,
    get_cached_dataset,
    get_cache_statistics,
    invalidate_cache,
)

__all__ = [
    "cache_dataset",
    "get_cached_dataset",
    "invalidate_cache",
    "clear_cache",
    "get_cache_statistics",
]