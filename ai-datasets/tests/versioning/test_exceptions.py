"""
Unit tests for ai_datasets.versioning.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.versioning.exceptions import (
    DatasetVersioningError,
    VersionAlreadyExistsError,
    VersionComparisonError,
    VersionConfigurationError,
    VersionNotFoundError,
    VersionProviderError,
    VersionRollbackError,
    VersionValidationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        VersionValidationError,
        VersionAlreadyExistsError,
        VersionNotFoundError,
        VersionComparisonError,
        VersionRollbackError,
        VersionConfigurationError,
        VersionProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetVersioningError],
) -> None:
    """Every custom exception should inherit from DatasetVersioningError."""
    assert issubclass(
        exception_class,
        DatasetVersioningError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetVersioningError,
        match="versioning failure",
    ):
        raise DatasetVersioningError(
            "versioning failure",
        )