"""
Unit tests for ai_datasets.config.constants.
"""

from __future__ import annotations

from ai_datasets.config import constants


def test_supported_operations() -> None:
    """Supported configuration operations should contain all operations."""
    assert constants.LOAD in constants.SUPPORTED_OPERATIONS
    assert constants.GET in constants.SUPPORTED_OPERATIONS
    assert constants.UPDATE in constants.SUPPORTED_OPERATIONS
    assert constants.RESET in constants.SUPPORTED_OPERATIONS
    assert constants.EXPORT in constants.SUPPORTED_OPERATIONS


def test_default_configuration() -> None:
    """Default configuration constants should be valid."""
    assert constants.DEFAULT_CONFIG_NAME == "default"
    assert constants.DEFAULT_ENCODING == "utf-8"
    assert constants.DEFAULT_INDENT == 4


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_CONFIG_NAME == "config_name"
    assert constants.METADATA_ENCODING == "encoding"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_STATUS == "status"