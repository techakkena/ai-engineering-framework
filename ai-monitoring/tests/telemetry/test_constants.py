"""
Unit tests for ai_monitoring.telemetry.constants.
"""

from __future__ import annotations

from ai_monitoring.telemetry import constants


def test_supported_operations() -> None:
    """Supported operations should contain all telemetry operations."""
    assert constants.COLLECT in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS
    assert constants.EXPORT in constants.SUPPORTED_OPERATIONS
    assert constants.RESET in constants.SUPPORTED_OPERATIONS


def test_supported_types() -> None:
    """Supported telemetry types should be valid."""
    assert constants.METRIC in constants.SUPPORTED_TYPES
    assert constants.TRACE in constants.SUPPORTED_TYPES
    assert constants.LOG in constants.SUPPORTED_TYPES
    assert constants.EVENT in constants.SUPPORTED_TYPES


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_TELEMETRY_ID == "telemetry_id"
    assert constants.METADATA_TYPE == "type"
    assert constants.METADATA_TIMESTAMP == "timestamp"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_STATUS == "status"