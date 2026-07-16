"""
Unit tests for ai_datasets.loaders.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.loaders.exceptions import (
    CSVLoaderError,
    DatabaseLoaderError,
    DatasetLoaderError,
    DatasetLoadingError,
    DatasetSourceError,
    JSONLoaderError,
    LoaderValidationError,
    ParquetLoaderError,
    TextLoaderError,
    UnsupportedLoaderError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        LoaderValidationError,
        UnsupportedLoaderError,
        DatasetLoadingError,
        CSVLoaderError,
        JSONLoaderError,
        ParquetLoaderError,
        TextLoaderError,
        DatabaseLoaderError,
        DatasetSourceError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetLoaderError],
) -> None:
    """Every custom exception should inherit from DatasetLoaderError."""
    assert issubclass(
        exception_class,
        DatasetLoaderError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetLoaderError,
        match="loader failure",
    ):
        raise DatasetLoaderError("loader failure")