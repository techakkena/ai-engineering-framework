"""
Unit tests for ai_datasets.transformers.constants.
"""

from __future__ import annotations

from ai_datasets.transformers import constants


def test_supported_operations() -> None:
    """Supported operations should contain all transformer operations."""
    assert constants.TRANSFORM in constants.SUPPORTED_OPERATIONS
    assert constants.FILTER in constants.SUPPORTED_OPERATIONS
    assert constants.MAP in constants.SUPPORTED_OPERATIONS
    assert constants.NORMALIZE in constants.SUPPORTED_OPERATIONS
    assert constants.BATCH in constants.SUPPORTED_OPERATIONS


def test_supported_normalization_methods() -> None:
    """Normalization methods should be supported."""
    assert (
        constants.NORMALIZATION_MIN_MAX
        in constants.SUPPORTED_NORMALIZATION_METHODS
    )
    assert (
        constants.NORMALIZATION_Z_SCORE
        in constants.SUPPORTED_NORMALIZATION_METHODS
    )
    assert (
        constants.NORMALIZATION_L2
        in constants.SUPPORTED_NORMALIZATION_METHODS
    )


def test_default_configuration() -> None:
    """Default transformer configuration should be valid."""
    assert constants.DEFAULT_BATCH_SIZE > 0
    assert constants.DEFAULT_SHUFFLE is False
    assert constants.DEFAULT_DROP_LAST is False


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_OPERATION == "operation"
    assert constants.METADATA_RECORD_COUNT == "record_count"
    assert constants.METADATA_BATCH_SIZE == "batch_size"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_STATUS == "status"