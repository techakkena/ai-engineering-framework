"""
Unit tests for ai_datasets.validators.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.validators.exceptions import (
    ConstraintValidationError,
    DatasetValidationError,
    DatasetValidatorError,
    IntegrityValidationError,
    MetadataValidationError,
    SchemaValidationError,
    UnsupportedValidationTypeError,
    ValidationProcessingError,
    ValidatorConfigurationError,
    ValidatorProviderError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        DatasetValidationError,
        SchemaValidationError,
        IntegrityValidationError,
        ConstraintValidationError,
        MetadataValidationError,
        ValidatorConfigurationError,
        UnsupportedValidationTypeError,
        ValidationProcessingError,
        ValidatorProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetValidatorError],
) -> None:
    """Every custom exception should inherit from DatasetValidatorError."""
    assert issubclass(
        exception_class,
        DatasetValidatorError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetValidatorError,
        match="validator failure",
    ):
        raise DatasetValidatorError(
            "validator failure",
        )