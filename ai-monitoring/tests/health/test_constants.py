"""
Unit tests for ai_monitoring.health.constants.
"""

from __future__ import annotations

from ai_monitoring.health import constants


def test_supported_operations() -> None:
    """Supported operations should contain all health operations."""
    assert constants.CHECK in constants.SUPPORTED_OPERATIONS
    assert constants.RUN in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS
    assert constants.REGISTER in constants.SUPPORTED_OPERATIONS


def test_supported_statuses() -> None:
    """Supported health statuses should be valid."""
    assert constants.HEALTHY in constants.SUPPORTED_STATUSES
    assert constants.DEGRADED in constants.SUPPORTED_STATUSES
    assert constants.UNHEALTHY in constants.SUPPORTED_STATUSES
    assert constants.UNKNOWN in constants.SUPPORTED_STATUSES


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_CHECK_NAME == "check_name"
    assert constants.METADATA_STATUS == "status"
    assert constants.METADATA_TIMESTAMP == "timestamp"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_MESSAGE == "message"