"""
Unit tests for ai_monitoring.profiling.constants.
"""

from __future__ import annotations

from ai_monitoring.profiling import constants


def test_supported_operations() -> None:
    """Supported operations should contain all profiling operations."""
    assert constants.START in constants.SUPPORTED_OPERATIONS
    assert constants.STOP in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS
    assert constants.RESET in constants.SUPPORTED_OPERATIONS


def test_supported_profile_types() -> None:
    """Supported profile types should be valid."""
    assert constants.CPU in constants.SUPPORTED_PROFILE_TYPES
    assert constants.MEMORY in constants.SUPPORTED_PROFILE_TYPES
    assert constants.NETWORK in constants.SUPPORTED_PROFILE_TYPES
    assert constants.IO in constants.SUPPORTED_PROFILE_TYPES


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_PROFILE_ID == "profile_id"
    assert constants.METADATA_PROFILE_TYPE == "profile_type"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_TIMESTAMP == "timestamp"
    assert constants.METADATA_STATUS == "status"