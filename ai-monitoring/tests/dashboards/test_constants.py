"""
Unit tests for ai_monitoring.dashboards.constants.
"""

from __future__ import annotations

from ai_monitoring.dashboards import constants


def test_supported_operations() -> None:
    """Supported operations should contain all dashboard operations."""
    assert constants.CREATE in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.UPDATE in constants.SUPPORTED_OPERATIONS
    assert constants.DELETE in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS


def test_supported_dashboard_types() -> None:
    """Supported dashboard types should be valid."""
    assert constants.SYSTEM in constants.SUPPORTED_DASHBOARD_TYPES
    assert constants.APPLICATION in constants.SUPPORTED_DASHBOARD_TYPES
    assert constants.BUSINESS in constants.SUPPORTED_DASHBOARD_TYPES
    assert constants.CUSTOM in constants.SUPPORTED_DASHBOARD_TYPES


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_DASHBOARD_ID == "dashboard_id"
    assert constants.METADATA_NAME == "name"
    assert constants.METADATA_TYPE == "type"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_STATUS == "status"