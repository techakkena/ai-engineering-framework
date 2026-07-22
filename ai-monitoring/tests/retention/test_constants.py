"""
Unit tests for ai_monitoring.retention.constants.
"""

from __future__ import annotations

from ai_monitoring.retention import constants


def test_supported_operations() -> None:
    """Supported operations should contain all retention operations."""
    assert constants.CREATE in constants.SUPPORTED_OPERATIONS
    assert constants.APPLY in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS
    assert constants.DELETE in constants.SUPPORTED_OPERATIONS


def test_supported_policy_types() -> None:
    """Supported retention policy types should be valid."""
    assert constants.TIME_BASED in constants.SUPPORTED_POLICY_TYPES
    assert constants.SIZE_BASED in constants.SUPPORTED_POLICY_TYPES
    assert constants.HYBRID in constants.SUPPORTED_POLICY_TYPES


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_POLICY_ID == "policy_id"
    assert constants.METADATA_POLICY_TYPE == "policy_type"
    assert constants.METADATA_STATUS == "status"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_TIMESTAMP == "timestamp"