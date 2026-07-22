"""
Unit tests for ai_monitoring.collectors.constants.
"""

from __future__ import annotations

from ai_monitoring.collectors import constants


def test_supported_operations() -> None:
    """Supported operations should contain all collector operations."""
    assert constants.REGISTER in constants.SUPPORTED_OPERATIONS
    assert constants.COLLECT in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS
    assert constants.REMOVE in constants.SUPPORTED_OPERATIONS


def test_supported_collectors() -> None:
    """Supported collector types should be valid."""
    assert constants.SYSTEM in constants.SUPPORTED_COLLECTORS
    assert constants.APPLICATION in constants.SUPPORTED_COLLECTORS
    assert constants.CUSTOM in constants.SUPPORTED_COLLECTORS
    assert constants.REMOTE in constants.SUPPORTED_COLLECTORS


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_COLLECTOR_ID == "collector_id"
    assert constants.METADATA_COLLECTOR_TYPE == "collector_type"
    assert constants.METADATA_STATUS == "status"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_TIMESTAMP == "timestamp"