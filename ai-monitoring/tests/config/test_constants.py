"""
Unit tests for ai_monitoring.config.constants.
"""

from __future__ import annotations

from ai_monitoring.config import constants


def test_supported_operations() -> None:
    """Supported operations should contain all configuration operations."""
    assert constants.LOAD in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.UPDATE in constants.SUPPORTED_OPERATIONS
    assert constants.EXPORT in constants.SUPPORTED_OPERATIONS
    assert constants.LIST in constants.SUPPORTED_OPERATIONS


def test_default_values() -> None:
    """Default configuration values should be correct."""
    assert constants.DEFAULT_CONFIG_NAME == "default"
    assert constants.DEFAULT_ENCODING == "utf-8"
    assert constants.DEFAULT_INDENT == 4


def test_metadata_constants() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_CONFIG_NAME == "config_name"
    assert constants.METADATA_STATUS == "status"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_TIMESTAMP == "timestamp"