"""
Constants for the ai_datasets.splitters module.

This module defines framework-independent constants used by dataset
splitting operations.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Split operations
# ---------------------------------------------------------------------------

SPLIT_DATASET: Final[str] = "split_dataset"
TRAIN_TEST_SPLIT: Final[str] = "train_test_split"
STRATIFIED_SPLIT: Final[str] = "stratified_split"
K_FOLD_SPLIT: Final[str] = "k_fold_split"
TIME_SERIES_SPLIT: Final[str] = "time_series_split"

SUPPORTED_SPLITS: Final[tuple[str, ...]] = (
    SPLIT_DATASET,
    TRAIN_TEST_SPLIT,
    STRATIFIED_SPLIT,
    K_FOLD_SPLIT,
    TIME_SERIES_SPLIT,
)

# ---------------------------------------------------------------------------
# Default split ratios
# ---------------------------------------------------------------------------

DEFAULT_TRAIN_RATIO: Final[float] = 0.80
DEFAULT_VALIDATION_RATIO: Final[float] = 0.10
DEFAULT_TEST_RATIO: Final[float] = 0.10

# ---------------------------------------------------------------------------
# Cross-validation defaults
# ---------------------------------------------------------------------------

DEFAULT_K_FOLDS: Final[int] = 5
DEFAULT_SHUFFLE: Final[bool] = True
DEFAULT_RANDOM_SEED: Final[int] = 42

# ---------------------------------------------------------------------------
# Time-series defaults
# ---------------------------------------------------------------------------

DEFAULT_GAP: Final[int] = 0

# ---------------------------------------------------------------------------
# Metadata keys
# ---------------------------------------------------------------------------

METADATA_SPLIT_TYPE: Final[str] = "split_type"
METADATA_TRAIN_SIZE: Final[str] = "train_size"
METADATA_VALIDATION_SIZE: Final[str] = "validation_size"
METADATA_TEST_SIZE: Final[str] = "test_size"
METADATA_FOLDS: Final[str] = "folds"
METADATA_RANDOM_SEED: Final[str] = "random_seed"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_STATUS: Final[str] = "status"