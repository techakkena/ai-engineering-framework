"""
Unit tests for ai_monitoring.tracing.constants.
"""

from __future__ import annotations

from ai_monitoring.tracing import constants


def test_supported_operations() -> None:
    """Supported operations should contain all tracing operations."""
    assert constants.START in constants.SUPPORTED_OPERATIONS
    assert constants.SPAN in constants.SUPPORTED_OPERATIONS
    assert constants.END in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS


def test_supported_span_types() -> None:
    """Supported span types should be valid."""
    assert constants.LLM in constants.SUPPORTED_SPAN_TYPES
    assert constants.TOOL in constants.SUPPORTED_SPAN_TYPES
    assert constants.WORKFLOW in constants.SUPPORTED_SPAN_TYPES
    assert constants.DATABASE in constants.SUPPORTED_SPAN_TYPES


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_TRACE_ID == "trace_id"
    assert constants.METADATA_SPAN_ID == "span_id"
    assert constants.METADATA_PARENT_ID == "parent_id"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_STATUS == "status"