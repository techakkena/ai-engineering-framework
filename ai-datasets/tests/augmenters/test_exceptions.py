"""
Unit tests for ai_datasets.augmenters.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.augmenters.exceptions import (
    AudioAugmentationError,
    AugmentationValidationError,
    AugmenterProviderError,
    DatasetAugmentationError,
    DatasetAugmenterError,
    ImageAugmentationError,
    TabularAugmentationError,
    TextAugmentationError,
    UnsupportedAugmentationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        AugmentationValidationError,
        UnsupportedAugmentationError,
        DatasetAugmentationError,
        TextAugmentationError,
        ImageAugmentationError,
        AudioAugmentationError,
        TabularAugmentationError,
        AugmenterProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetAugmenterError],
) -> None:
    """Every custom exception should inherit from DatasetAugmenterError."""
    assert issubclass(
        exception_class,
        DatasetAugmenterError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetAugmenterError,
        match="augmentation failure",
    ):
        raise DatasetAugmenterError(
            "augmentation failure",
        )