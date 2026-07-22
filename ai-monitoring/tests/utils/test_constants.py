"""
Unit tests for ai_monitoring.utils.constants.
"""

from __future__ import annotations

from ai_monitoring.utils import constants


def test_supported_operations() -> None:
    """Supported operations should contain all utility operations."""
    assert constants.BUILD in constants.SUPPORTED_OPERATIONS
    assert constants.FORMAT in constants.SUPPORTED_OPERATIONS
    assert constants.GENERATE in constants.SUPPORTED_OPERATIONS
    assert constants.VALIDATE in constants.SUPPORTED_OPERATIONS
    assert constants.TIMESTAMP in constants.SUPPORTED_OPERATIONS


def test_default_values() -> None:
    """Default constants should be valid."""
    assert constants.DEFAULT_PREFIX == "monitor"
    assert constants.DEFAULT_SEPARATOR == "-"
    assert constants.DEFAULT_TIME_UNIT == "ms"


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_ID == "id"
    assert constants.METADATA_CREATED_AT == "created_at"
    assert constants.METADATA_STATUS == "status"
    assert constants.METADATA_DURATION == "duration_ms"