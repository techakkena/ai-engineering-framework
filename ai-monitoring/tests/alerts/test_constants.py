"""
Unit tests for ai_monitoring.alerts.constants.
"""

from __future__ import annotations

from ai_monitoring.alerts import constants


def test_supported_operations() -> None:
    """Supported operations should contain all alert operations."""
    assert constants.CREATE in constants.SUPPORTED_OPERATIONS
    assert constants.ACKNOWLEDGE in constants.SUPPORTED_OPERATIONS
    assert constants.RESOLVE in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS


def test_supported_severities() -> None:
    """Supported severities should be valid."""
    assert constants.INFO in constants.SUPPORTED_SEVERITIES
    assert constants.WARNING in constants.SUPPORTED_SEVERITIES
    assert constants.ERROR in constants.SUPPORTED_SEVERITIES
    assert constants.CRITICAL in constants.SUPPORTED_SEVERITIES


def test_supported_statuses() -> None:
    """Supported alert statuses should be valid."""
    assert constants.OPEN in constants.SUPPORTED_STATUSES
    assert constants.ACKNOWLEDGED in constants.SUPPORTED_STATUSES
    assert constants.RESOLVED in constants.SUPPORTED_STATUSES


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_ALERT_ID == "alert_id"
    assert constants.METADATA_SEVERITY == "severity"
    assert constants.METADATA_STATUS == "status"
    assert constants.METADATA_TIMESTAMP == "timestamp"
    assert constants.METADATA_DURATION == "duration_ms"