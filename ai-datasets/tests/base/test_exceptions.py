"""
Unit tests for ai_datasets.base.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.base.exceptions import (
    DatasetCreationError,
    DatasetError,
    DatasetLoadingError,
    DatasetMetadataError,
    DatasetProcessingError,
    DatasetProviderError,
    DatasetSavingError,
    DatasetValidationError,
    InvalidDatasetError,
    UnsupportedDatasetTypeError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        DatasetValidationError,
        UnsupportedDatasetTypeError,
        InvalidDatasetError,
        DatasetProcessingError,
        DatasetCreationError,
        DatasetLoadingError,
        DatasetSavingError,
        DatasetMetadataError,
        DatasetProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetError],
) -> None:
    """Every custom exception should inherit from DatasetError."""
    assert issubclass(exception_class, DatasetError)


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(DatasetError, match="dataset failure"):
        raise DatasetError("dataset failure")