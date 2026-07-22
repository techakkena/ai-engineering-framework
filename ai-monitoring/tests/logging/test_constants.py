"""
Unit tests for ai_monitoring.logging.constants.
"""

from __future__ import annotations

from ai_monitoring.logging import constants


def test_supported_operations() -> None:
    """Supported operations should contain all logging operations."""
    assert constants.LOG in constants.SUPPORTED_OPERATIONS
    assert constants.EVENT in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS
    assert constants.CLEAR in constants.SUPPORTED_OPERATIONS


def test_supported_levels() -> None:
    """Supported log levels should contain all levels."""
    assert constants.DEBUG in constants.SUPPORTED_LEVELS
    assert constants.INFO in constants.SUPPORTED_LEVELS
    assert constants.WARNING in constants.SUPPORTED_LEVELS
    assert constants.ERROR in constants.SUPPORTED_LEVELS
    assert constants.CRITICAL in constants.SUPPORTED_LEVELS


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_LOG_ID == "log_id"
    assert constants.METADATA_LEVEL == "level"
    assert constants.METADATA_TIMESTAMP == "timestamp"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_STATUS == "status"