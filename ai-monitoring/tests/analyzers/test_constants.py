"""
Unit tests for ai_monitoring.analyzers.constants.
"""

from __future__ import annotations

from ai_monitoring.analyzers import constants


def test_supported_operations() -> None:
    """Supported operations should contain all analyzer operations."""
    assert constants.RUN in constants.SUPPORTED_OPERATIONS
    assert constants.ANALYZE in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS
    assert constants.COMPARE in constants.SUPPORTED_OPERATIONS


def test_supported_analysis_types() -> None:
    """Supported analysis types should be valid."""
    assert constants.PERFORMANCE in constants.SUPPORTED_ANALYSIS_TYPES
    assert constants.RESOURCE in constants.SUPPORTED_ANALYSIS_TYPES
    assert constants.USAGE in constants.SUPPORTED_ANALYSIS_TYPES
    assert constants.ANOMALY in constants.SUPPORTED_ANALYSIS_TYPES


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_ANALYSIS_ID == "analysis_id"
    assert constants.METADATA_ANALYSIS_TYPE == "analysis_type"
    assert constants.METADATA_STATUS == "status"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_TIMESTAMP == "timestamp"