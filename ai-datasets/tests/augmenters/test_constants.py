"""
Unit tests for ai_datasets.augmenters.constants.
"""

from __future__ import annotations

from ai_datasets.augmenters import constants


def test_supported_augmentations() -> None:
    """Supported augmentations should contain all augmentation types."""
    assert constants.AUGMENT_TEXT in constants.SUPPORTED_AUGMENTATIONS
    assert constants.AUGMENT_IMAGE in constants.SUPPORTED_AUGMENTATIONS
    assert constants.AUGMENT_AUDIO in constants.SUPPORTED_AUGMENTATIONS
    assert constants.AUGMENT_TABULAR in constants.SUPPORTED_AUGMENTATIONS


def test_default_configuration() -> None:
    """Default augmentation configuration should be valid."""
    assert constants.DEFAULT_AUGMENTATIONS > 0
    assert constants.DEFAULT_RANDOM_SEED == 42


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_TYPE == "augmentation_type"
    assert constants.METADATA_COUNT == "augmentation_count"
    assert constants.METADATA_DURATION == "duration_ms"