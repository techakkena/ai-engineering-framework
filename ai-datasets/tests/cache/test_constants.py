"""
Unit tests for ai_datasets.cache.constants.
"""

from __future__ import annotations

from ai_datasets.cache import constants


def test_supported_operations() -> None:
    """Supported cache operations should contain all operations."""
    assert constants.CACHE in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.INVALIDATE in constants.SUPPORTED_OPERATIONS
    assert constants.CLEAR in constants.SUPPORTED_OPERATIONS
    assert constants.STATISTICS in constants.SUPPORTED_OPERATIONS


def test_default_configuration() -> None:
    """Default cache configuration should be valid."""
    assert constants.DEFAULT_TTL > 0
    assert constants.DEFAULT_MAX_ENTRIES > 0


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_CACHE_KEY == "cache_key"
    assert constants.METADATA_TTL == "ttl"
    assert constants.METADATA_CACHE_SIZE == "cache_size"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_STATUS == "status"