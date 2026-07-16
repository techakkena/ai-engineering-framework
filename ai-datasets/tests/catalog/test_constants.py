"""
Unit tests for ai_datasets.catalog.constants.
"""

from __future__ import annotations

from ai_datasets.catalog import constants


def test_supported_operations() -> None:
    """Supported operations should contain all catalog operations."""
    assert constants.REGISTER in constants.SUPPORTED_OPERATIONS
    assert constants.UNREGISTER in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS
    assert constants.SEARCH in constants.SUPPORTED_OPERATIONS


def test_supported_statuses() -> None:
    """Supported dataset statuses should be valid."""
    assert constants.STATUS_ACTIVE in constants.SUPPORTED_STATUSES
    assert constants.STATUS_ARCHIVED in constants.SUPPORTED_STATUSES
    assert constants.STATUS_DEPRECATED in constants.SUPPORTED_STATUSES


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_DATASET_ID == "dataset_id"
    assert constants.METADATA_VERSION == "version"
    assert constants.METADATA_OWNER == "owner"
    assert constants.METADATA_STATUS == "status"
    assert constants.METADATA_DURATION == "duration_ms"