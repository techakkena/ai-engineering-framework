"""
Unit tests for ai_datasets.catalog.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.catalog.exceptions import (
    CatalogConfigurationError,
    CatalogProviderError,
    CatalogRegistrationError,
    CatalogSearchError,
    CatalogValidationError,
    DatasetAlreadyExistsError,
    DatasetCatalogError,
    DatasetNotFoundError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        CatalogValidationError,
        DatasetAlreadyExistsError,
        DatasetNotFoundError,
        CatalogRegistrationError,
        CatalogSearchError,
        CatalogConfigurationError,
        CatalogProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetCatalogError],
) -> None:
    """Every custom exception should inherit from DatasetCatalogError."""
    assert issubclass(
        exception_class,
        DatasetCatalogError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetCatalogError,
        match="catalog failure",
    ):
        raise DatasetCatalogError(
            "catalog failure",
        )