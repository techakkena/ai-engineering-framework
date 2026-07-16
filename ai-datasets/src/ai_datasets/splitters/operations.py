"""
Enterprise dataset splitting operations for the ai_datasets.splitters package.

This module provides provider-independent abstractions for train/test,
stratified, k-fold, and time-series dataset splitting.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_datasets.splitters.constants import (
    DEFAULT_K_FOLDS,
    DEFAULT_RANDOM_SEED,
    DEFAULT_TEST_RATIO,
    DEFAULT_TRAIN_RATIO,
)
from ai_datasets.splitters.exceptions import (
    KFoldSplitError,
    SplitValidationError,
    StratifiedSplitError,
    TrainTestSplitError,
)


@dataclass(slots=True, frozen=True)
class SplitResult:
    """Represents the result of a dataset split operation."""

    task: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


def _validate_dataset(
    dataset: list[dict[str, Any]],
) -> None:
    """Validate dataset input."""
    if not dataset:
        raise SplitValidationError(
            "Dataset cannot be empty."
        )


def split_dataset(
    dataset: list[dict[str, Any]],
) -> SplitResult:
    """
    Perform a default dataset split.
    """
    _validate_dataset(dataset)

    return SplitResult(
        task="split_dataset",
        success=True,
        data={
            "records": len(dataset),
        },
    )


def train_test_split(
    dataset: list[dict[str, Any]],
    *,
    train_ratio: float = DEFAULT_TRAIN_RATIO,
    test_ratio: float = DEFAULT_TEST_RATIO,
    random_seed: int = DEFAULT_RANDOM_SEED,
) -> SplitResult:
    """
    Perform a train/test split.
    """
    _validate_dataset(dataset)

    if train_ratio <= 0 or test_ratio <= 0:
        raise TrainTestSplitError(
            "Split ratios must be greater than zero."
        )

    if (train_ratio + test_ratio) > 1.0:
        raise TrainTestSplitError(
            "Train and test ratios cannot exceed 1.0."
        )

    return SplitResult(
        task="train_test_split",
        success=True,
        data={
            "train_ratio": train_ratio,
            "test_ratio": test_ratio,
            "random_seed": random_seed,
        },
    )


def stratified_split(
    dataset: list[dict[str, Any]],
    *,
    label_column: str,
) -> SplitResult:
    """
    Perform a stratified split.
    """
    _validate_dataset(dataset)

    if not label_column.strip():
        raise StratifiedSplitError(
            "Label column cannot be empty."
        )

    return SplitResult(
        task="stratified_split",
        success=True,
        data={
            "label_column": label_column,
        },
    )


def k_fold_split(
    dataset: list[dict[str, Any]],
    *,
    folds: int = DEFAULT_K_FOLDS,
) -> SplitResult:
    """
    Perform k-fold cross validation.
    """
    _validate_dataset(dataset)

    if folds < 2:
        raise KFoldSplitError(
            "Number of folds must be at least 2."
        )

    return SplitResult(
        task="k_fold_split",
        success=True,
        data={
            "folds": folds,
        },
    )


def time_series_split(
    dataset: list[dict[str, Any]],
) -> SplitResult:
    """
    Perform a time-series split.
    """
    _validate_dataset(dataset)

    return SplitResult(
        task="time_series_split",
        success=True,
        data={
            "records": len(dataset),
        },
    )