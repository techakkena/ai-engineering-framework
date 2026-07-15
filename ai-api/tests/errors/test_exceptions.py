"""
Unit tests for ai_api.errors.exceptions.
"""

from __future__ import annotations

import pytest

from ai_api.errors.exceptions import (
    ErrorCategoryError,
    ErrorConfigurationError,
    ErrorHandlingError,
    ErrorMappingError,
    ErrorSerializationError,
    ErrorValidationError,
    InvalidErrorCodeError,
    InvalidErrorTypeError,
)


def test_error_handling_error_default_message() -> None:
    """Test ErrorHandlingError with the default message."""
    error = ErrorHandlingError()

    assert str(error) == "An error handling error occurred."


def test_error_handling_error_custom_message() -> None:
    """Test ErrorHandlingError with a custom message."""
    error = ErrorHandlingError("Custom error.")

    assert str(error) == "Custom error."


@pytest.mark.parametrize(
    "error_code",
    [
        "",
        "ABC1000",
        "ERRABC",
        "ERR99999",
    ],
)
def test_invalid_error_code_error(
    error_code: str,
) -> None:
    """Test InvalidErrorCodeError."""
    error = InvalidErrorCodeError(error_code)

    assert isinstance(error, ErrorHandlingError)
    assert error.error_code == error_code
    assert (
        str(error)
        == f"Invalid error code: '{error_code}'."
    )


@pytest.mark.parametrize(
    "error_type",
    [
        "",
        "database_error",
        "network_error",
        "custom_error",
    ],
)
def test_invalid_error_type_error(
    error_type: str,
) -> None:
    """Test InvalidErrorTypeError."""
    error = InvalidErrorTypeError(error_type)

    assert isinstance(error, ErrorHandlingError)
    assert error.error_type == error_type
    assert (
        str(error)
        == f"Invalid error type: '{error_type}'."
    )


@pytest.mark.parametrize(
    "source",
    [
        "ValueError",
        "RuntimeError",
        "ValidationError",
    ],
)
def test_error_mapping_error(
    source: str,
) -> None:
    """Test ErrorMappingError."""
    error = ErrorMappingError(source)

    assert isinstance(error, ErrorHandlingError)
    assert error.source == source
    assert (
        str(error)
        == f"Unable to map error: '{source}'."
    )


def test_error_configuration_error() -> None:
    """Test ErrorConfigurationError."""
    configuration = "error_policy"

    error = ErrorConfigurationError(
        configuration,
    )

    assert isinstance(error, ErrorHandlingError)
    assert error.configuration == configuration
    assert (
        str(error)
        == (
            "Invalid error configuration: "
            f"'{configuration}'."
        )
    )


@pytest.mark.parametrize(
    "reason",
    [
        "JSON encoding failed",
        "Unknown serializer",
        "Encoding error",
    ],
)
def test_error_serialization_error(
    reason: str,
) -> None:
    """Test ErrorSerializationError."""
    error = ErrorSerializationError(reason)

    assert isinstance(error, ErrorHandlingError)
    assert error.reason == reason
    assert (
        str(error)
        == (
            f"Error serialization failed: "
            f"{reason}."
        )
    )


def test_error_validation_error() -> None:
    """Test ErrorValidationError."""
    field = "code"
    reason = "Missing value"

    error = ErrorValidationError(
        field,
        reason,
    )

    assert isinstance(error, ErrorHandlingError)
    assert error.field == field
    assert error.reason == reason
    assert (
        str(error)
        == (
            f"Error validation failed for "
            f"'{field}': {reason}."
        )
    )


@pytest.mark.parametrize(
    "category",
    [
        "",
        "database",
        "filesystem",
        "external",
    ],
)
def test_error_category_error(
    category: str,
) -> None:
    """Test ErrorCategoryError."""
    error = ErrorCategoryError(category)

    assert isinstance(error, ErrorHandlingError)
    assert error.category == category
    assert (
        str(error)
        == f"Invalid error category: '{category}'."
    )