"""
Unit tests for ai_datasets.utils.constants.
"""

from __future__ import annotations

from ai_datasets.utils import constants


def test_supported_operations() -> None:
    """Supported utility operations should contain all operations."""
    assert constants.STATISTICS in constants.SUPPORTED_OPERATIONS
    assert constants.SUMMARY in constants.SUPPORTED_OPERATIONS
    assert constants.SCHEMA in constants.SUPPORTED_OPERATIONS
    assert constants.VALIDATE_DATASET in constants.SUPPORTED_OPERATIONS
    assert constants.VALIDATE_RECORD in constants.SUPPORTED_OPERATIONS


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_RECORD_COUNT == "record_count"
    assert constants.METADATA_FIELD_COUNT == "field_count"
    assert constants.METADATA_SCHEMA == "schema"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_STATUS == "status"