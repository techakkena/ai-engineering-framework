"""
Unit tests for ai_datasets.registry.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.registry.exceptions import (
    DatasetAlreadyRegisteredError,
    DatasetNotRegisteredError,
    DatasetRegistryError,
    RegistryConfigurationError,
    RegistryOperationError,
    RegistryProviderError,
    RegistryValidationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        RegistryValidationError,
        DatasetAlreadyRegisteredError,
        DatasetNotRegisteredError,
        RegistryOperationError,
        RegistryConfigurationError,
        RegistryProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetRegistryError],
) -> None:
    """Every custom exception should inherit from DatasetRegistryError."""
    assert issubclass(
        exception_class,
        DatasetRegistryError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetRegistryError,
        match="registry failure",
    ):
        raise DatasetRegistryError(
            "registry failure",
        )