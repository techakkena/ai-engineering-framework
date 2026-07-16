"""
Unit tests for ai_datasets.splitters.constants.
"""

from __future__ import annotations

from ai_datasets.splitters import constants


def test_supported_splits() -> None:
    """Supported split operations should contain all split strategies."""
    assert constants.SPLIT_DATASET in constants.SUPPORTED_SPLITS
    assert constants.TRAIN_TEST_SPLIT in constants.SUPPORTED_SPLITS
    assert constants.STRATIFIED_SPLIT in constants.SUPPORTED_SPLITS
    assert constants.K_FOLD_SPLIT in constants.SUPPORTED_SPLITS
    assert constants.TIME_SERIES_SPLIT in constants.SUPPORTED_SPLITS


def test_default_ratios() -> None:
    """Default split ratios should sum to one."""
    total = (
        constants.DEFAULT_TRAIN_RATIO
        + constants.DEFAULT_VALIDATION_RATIO
        + constants.DEFAULT_TEST_RATIO
    )

    assert total == 1.0


def test_cross_validation_defaults() -> None:
    """Cross-validation defaults should be valid."""
    assert constants.DEFAULT_K_FOLDS >= 2
    assert constants.DEFAULT_SHUFFLE is True
    assert constants.DEFAULT_RANDOM_SEED == 42


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_SPLIT_TYPE == "split_type"
    assert constants.METADATA_TRAIN_SIZE == "train_size"
    assert constants.METADATA_VALIDATION_SIZE == "validation_size"
    assert constants.METADATA_TEST_SIZE == "test_size"
    assert constants.METADATA_FOLDS == "folds"
    assert constants.METADATA_RANDOM_SEED == "random_seed"
    assert constants.METADATA_DURATION == "duration_ms"
    assert constants.METADATA_STATUS == "status"