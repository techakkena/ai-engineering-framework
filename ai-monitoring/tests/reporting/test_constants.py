"""
Unit tests for ai_monitoring.reporting.constants.
"""

from __future__ import annotations

from ai_monitoring.reporting import constants


def test_supported_operations() -> None:
    """Supported operations should contain all reporting operations."""
    assert constants.CREATE in constants.SUPPORTED_OPERATIONS
    assert constants.EXPORT in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS
    assert constants.DELETE in constants.SUPPORTED_OPERATIONS


def test_supported_report_types() -> None:
    """Supported report types should be valid."""
    assert constants.SUMMARY in constants.SUPPORTED_REPORT_TYPES
    assert constants.DETAILED in constants.SUPPORTED_REPORT_TYPES
    assert constants.DAILY in constants.SUPPORTED_REPORT_TYPES
    assert constants.MONTHLY in constants.SUPPORTED_REPORT_TYPES


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_REPORT_ID == "report_id"
    assert constants.METADATA_REPORT_TYPE == "report_type"
    assert constants.METADATA_STATUS == "status"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_TIMESTAMP == "timestamp"