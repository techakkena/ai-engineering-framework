"""
Unit tests for ai_api.utils.exceptions.
"""

from __future__ import annotations

import pytest

from ai_api.utils.exceptions import (
    InvalidEncodingError,
    InvalidIdentifierError,
    InvalidUtilityOperationError,
    UtilityConfigurationError,
    UtilityError,
    UtilitySerializationError,
    UtilityTimeoutError,
    UtilityValidationError,
)


def test_utility_error_default_message() -> None:
    """Test UtilityError with the default message."""
    error = UtilityError()

    assert str(error) == "A utility error occurred."


def test_utility_error_custom_message() -> None:
    """Test UtilityError with a custom message."""
    error = UtilityError("Custom utility error.")

    assert str(error) == "Custom utility error."


@pytest.mark.parametrize(
    "encoding",
    [
        "",
        "utf-64",
        "ansi",
        "custom",
    ],
)
def test_invalid_encoding_error(
    encoding: str,
) -> None:
    """Test InvalidEncodingError."""
    error = InvalidEncodingError(encoding)

    assert isinstance(error, UtilityError)
    assert error.encoding == encoding
    assert (
        str(error)
        == f"Invalid encoding: '{encoding}'."
    )


@pytest.mark.parametrize(
    "identifier",
    [
        "",
        "123abc",
        "user-name",
        "@invalid",
    ],
)
def test_invalid_identifier_error(
    identifier: str,
) -> None:
    """Test InvalidIdentifierError."""
    error = InvalidIdentifierError(identifier)

    assert isinstance(error, UtilityError)
    assert error.identifier == identifier
    assert (
        str(error)
        == f"Invalid identifier: '{identifier}'."
    )


@pytest.mark.parametrize(
    "operation",
    [
        "encode",
        "decode",
        "slugify",
    ],
)
def test_invalid_utility_operation_error(
    operation: str,
) -> None:
    """Test InvalidUtilityOperationError."""
    error = InvalidUtilityOperationError(
        operation,
    )

    assert isinstance(error, UtilityError)
    assert error.operation == operation
    assert (
        str(error)
        == (
            f"Invalid utility operation: "
            f"'{operation}'."
        )
    )


def test_utility_configuration_error() -> None:
    """Test UtilityConfigurationError."""
    configuration = "encoding"

    error = UtilityConfigurationError(
        configuration,
    )

    assert isinstance(error, UtilityError)
    assert error.configuration == configuration
    assert (
        str(error)
        == (
            "Invalid utility configuration: "
            f"'{configuration}'."
        )
    )


def test_utility_validation_error() -> None:
    """Test UtilityValidationError."""
    field = "identifier"
    reason = "Invalid format"

    error = UtilityValidationError(
        field,
        reason,
    )

    assert isinstance(error, UtilityError)
    assert error.field == field
    assert error.reason == reason
    assert (
        str(error)
        == (
            f"Utility validation failed for "
            f"'{field}': {reason}."
        )
    )


@pytest.mark.parametrize(
    "reason",
    [
        "JSON serialization failed",
        "Encoding failed",
        "Unknown serializer",
    ],
)
def test_utility_serialization_error(
    reason: str,
) -> None:
    """Test UtilitySerializationError."""
    error = UtilitySerializationError(reason)

    assert isinstance(error, UtilityError)
    assert error.reason == reason
    assert (
        str(error)
        == (
            f"Utility serialization failed: "
            f"{reason}."
        )
    )


@pytest.mark.parametrize(
    "timeout",
    [
        1,
        30,
        60,
    ],
)
def test_utility_timeout_error(
    timeout: int,
) -> None:
    """Test UtilityTimeoutError."""
    error = UtilityTimeoutError(timeout)

    assert isinstance(error, UtilityError)
    assert error.timeout == timeout
    assert (
        str(error)
        == (
            f"Utility operation timed out after "
            f"{timeout} seconds."
        )
    )