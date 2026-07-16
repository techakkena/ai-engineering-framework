"""
Unit tests for ai_datasets.splitters.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.splitters.exceptions import (
    KFoldSplitError,
    SplitValidationError,
    StratifiedSplitError,
    TrainTestSplitError,
)
from ai_datasets.splitters.operations import (
    SplitResult,
    k_fold_split,
    split_dataset,
    stratified_split,
    train_test_split,
    time_series_split,
)


def _dataset() -> list[dict[str, object]]:
    """Return a sample dataset."""
    return [
        {"id": 1, "label": "A"},
        {"id": 2, "label": "B"},
        {"id": 3, "label": "A"},
    ]


def test_split_dataset_success() -> None:
    """Default dataset split should succeed."""
    result = split_dataset(_dataset())

    assert isinstance(result, SplitResult)
    assert result.success is True
    assert result.task == "split_dataset"


def test_split_dataset_empty() -> None:
    """Empty datasets should raise."""
    with pytest.raises(SplitValidationError):
        split_dataset([])


def test_train_test_split_success() -> None:
    """Train/test split should succeed."""
    result = train_test_split(_dataset())

    assert result.success is True
    assert result.task == "train_test_split"


def test_train_test_split_invalid_ratio() -> None:
    """Invalid split ratios should raise."""
    with pytest.raises(TrainTestSplitError):
        train_test_split(
            _dataset(),
            train_ratio=0.9,
            test_ratio=0.2,
        )


def test_stratified_split_success() -> None:
    """Stratified split should succeed."""
    result = stratified_split(
        _dataset(),
        label_column="label",
    )

    assert result.success is True
    assert result.task == "stratified_split"


def test_stratified_split_empty_label() -> None:
    """Empty label column should raise."""
    with pytest.raises(StratifiedSplitError):
        stratified_split(
            _dataset(),
            label_column="",
        )


def test_k_fold_split_success() -> None:
    """K-fold split should succeed."""
    result = k_fold_split(
        _dataset(),
        folds=5,
    )

    assert result.success is True
    assert result.task == "k_fold_split"


def test_k_fold_split_invalid_folds() -> None:
    """Invalid fold count should raise."""
    with pytest.raises(KFoldSplitError):
        k_fold_split(
            _dataset(),
            folds=1,
        )


def test_time_series_split_success() -> None:
    """Time-series split should succeed."""
    result = time_series_split(_dataset())

    assert result.success is True
    assert result.task == "time_series_split"