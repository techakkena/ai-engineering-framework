"""
Unit tests for ai_datasets.versioning.constants.
"""

from __future__ import annotations

from ai_datasets.versioning import constants


def test_supported_operations() -> None:
    """Supported operations should contain all versioning operations."""
    assert constants.CREATE in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS
    assert constants.COMPARE in constants.SUPPORTED_OPERATIONS
    assert constants.ROLLBACK in constants.SUPPORTED_OPERATIONS


def test_supported_statuses() -> None:
    """Supported statuses should be valid."""
    assert constants.STATUS_ACTIVE in constants.SUPPORTED_STATUSES
    assert constants.STATUS_ARCHIVED in constants.SUPPORTED_STATUSES
    assert constants.STATUS_DEPRECATED in constants.SUPPORTED_STATUSES


def test_default_version() -> None:
    """Default version should be valid."""
    assert constants.DEFAULT_VERSION == "1.0.0"


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_VERSION == "version"
    assert constants.METADATA_PREVIOUS_VERSION == "previous_version"
    assert constants.METADATA_DATASET_ID == "dataset_id"
    assert constants.METADATA_STATUS == "status"
    assert constants.METADATA_DURATION == "duration_ms"