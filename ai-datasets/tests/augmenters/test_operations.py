"""
Unit tests for ai_datasets.augmenters.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.augmenters.exceptions import (
    AugmentationValidationError,
)
from ai_datasets.augmenters.operations import (
    AugmentationResult,
    augment_audio,
    augment_dataset,
    augment_image,
    augment_tabular,
    augment_text,
)


def _dataset() -> list[dict[str, object]]:
    """Return a sample dataset."""
    return [
        {"id": 1, "text": "Hello"},
        {"id": 2, "text": "World"},
    ]


def test_augment_dataset_success() -> None:
    """Generic augmentation should succeed."""
    result = augment_dataset(_dataset())

    assert isinstance(result, AugmentationResult)
    assert result.success is True
    assert result.task == "augment_dataset"


def test_augment_dataset_empty() -> None:
    """Empty datasets should raise."""
    with pytest.raises(AugmentationValidationError):
        augment_dataset([])


def test_augment_text_success() -> None:
    """Text augmentation should succeed."""
    result = augment_text(_dataset())

    assert result.success is True
    assert result.task == "augment_text"


def test_augment_image_success() -> None:
    """Image augmentation should succeed."""
    result = augment_image(_dataset())

    assert result.success is True
    assert result.task == "augment_image"


def test_augment_audio_success() -> None:
    """Audio augmentation should succeed."""
    result = augment_audio(_dataset())

    assert result.success is True
    assert result.task == "augment_audio"


def test_augment_tabular_success() -> None:
    """Tabular augmentation should succeed."""
    result = augment_tabular(_dataset())

    assert result.success is True
    assert result.task == "augment_tabular"


@pytest.mark.parametrize(
    "operation",
    [
        augment_text,
        augment_image,
        augment_audio,
        augment_tabular,
    ],
)
def test_operations_empty_dataset(
    operation,
) -> None:
    """All augmentation operations should reject empty datasets."""
    with pytest.raises(AugmentationValidationError):
        operation([])