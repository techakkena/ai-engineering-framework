"""
Unit tests for ai_datasets.transformers.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.transformers.exceptions import (
    BatchTransformationError,
    NormalizationError,
    TransformerValidationError,
)
from ai_datasets.transformers.operations import (
    TransformerResult,
    batch_dataset,
    filter_dataset,
    map_dataset,
    normalize_dataset,
    transform_dataset,
)


def _dataset() -> list[dict[str, object]]:
    """Return a sample dataset."""
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]


def test_transform_dataset_success() -> None:
    """Dataset transformation should succeed."""
    result = transform_dataset(_dataset())

    assert isinstance(result, TransformerResult)
    assert result.success is True
    assert result.task == "transform"


def test_transform_dataset_empty() -> None:
    """Empty datasets should raise."""
    with pytest.raises(TransformerValidationError):
        transform_dataset([])


def test_filter_dataset_success() -> None:
    """Dataset filtering should succeed."""
    result = filter_dataset(_dataset())

    assert result.success is True
    assert result.task == "filter"


def test_map_dataset_success() -> None:
    """Dataset mapping should succeed."""
    result = map_dataset(_dataset())

    assert result.success is True
    assert result.task == "map"


def test_normalize_dataset_success() -> None:
    """Dataset normalization should succeed."""
    result = normalize_dataset(_dataset())

    assert result.success is True
    assert result.task == "normalize"


def test_normalize_dataset_invalid_method() -> None:
    """Unsupported normalization methods should raise."""
    with pytest.raises(NormalizationError):
        normalize_dataset(
            _dataset(),
            method="custom",
        )


def test_batch_dataset_success() -> None:
    """Dataset batching should succeed."""
    result = batch_dataset(
        _dataset(),
        batch_size=2,
    )

    assert result.success is True
    assert result.task == "batch"


def test_batch_dataset_invalid_batch_size() -> None:
    """Invalid batch sizes should raise."""
    with pytest.raises(BatchTransformationError):
        batch_dataset(
            _dataset(),
            batch_size=0,
        )