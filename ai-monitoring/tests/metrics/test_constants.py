"""
Unit tests for ai_monitoring.metrics.constants.
"""

from __future__ import annotations

from ai_monitoring.metrics import constants


def test_supported_operations() -> None:
    """Supported operations should contain all metric operations."""
    assert constants.COLLECT in constants.SUPPORTED_OPERATIONS
    assert constants.RECORD in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS
    assert constants.RESET in constants.SUPPORTED_OPERATIONS


def test_supported_metric_types() -> None:
    """Supported metric types should be valid."""
    assert constants.COUNTER in constants.SUPPORTED_METRIC_TYPES
    assert constants.GAUGE in constants.SUPPORTED_METRIC_TYPES
    assert constants.HISTOGRAM in constants.SUPPORTED_METRIC_TYPES
    assert constants.SUMMARY in constants.SUPPORTED_METRIC_TYPES


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_NAME == "metric_name"
    assert constants.METADATA_TYPE == "metric_type"
    assert constants.METADATA_VALUE == "value"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_STATUS == "status"