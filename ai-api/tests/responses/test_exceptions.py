"""
Unit tests for ai_api.responses.exceptions.
"""

from __future__ import annotations

import pytest

from ai_api.responses.exceptions import (
    InvalidContentTypeError,
    InvalidResponseError,
    ResponseConfigurationError,
    ResponseError,
    ResponseSerializationError,
    ResponseSizeExceededError,
    ResponseValidationError,
    UnsupportedResponseTypeError,
)


def test_response_error_default_message() -> None:
    """Test ResponseError with the default message."""
    error = ResponseError()

    assert str(error) == "A response error occurred."


def test_response_error_custom_message() -> None:
    """Test ResponseError with a custom message."""
    error = ResponseError("Custom response error.")

    assert str(error) == "Custom response error."


@pytest.mark.parametrize(
    "reason",
    [
        "missing status",
        "missing message",
        "invalid payload",
    ],
)
def test_invalid_response_error(
    reason: str,
) -> None:
    """Test InvalidResponseError."""
    error = InvalidResponseError(reason)

    assert isinstance(error, ResponseError)
    assert error.reason == reason
    assert str(error) == f"Invalid response: {reason}."


@pytest.mark.parametrize(
    "content_type",
    [
        "",
        "application/yaml",
        "application/pdf",
        "image/png",
    ],
)
def test_invalid_content_type_error(
    content_type: str,
) -> None:
    """Test InvalidContentTypeError."""
    error = InvalidContentTypeError(content_type)

    assert isinstance(error, ResponseError)
    assert error.content_type == content_type
    assert (
        str(error)
        == f"Invalid content type: '{content_type}'."
    )


@pytest.mark.parametrize(
    "response_type",
    [
        "stream",
        "binary",
        "protobuf",
    ],
)
def test_unsupported_response_type_error(
    response_type: str,
) -> None:
    """Test UnsupportedResponseTypeError."""
    error = UnsupportedResponseTypeError(
        response_type,
    )

    assert isinstance(error, ResponseError)
    assert error.response_type == response_type
    assert (
        str(error)
        == (
            f"Unsupported response type: "
            f"'{response_type}'."
        )
    )


@pytest.mark.parametrize(
    "reason",
    [
        "Invalid JSON",
        "Encoding failed",
        "Unknown serializer",
    ],
)
def test_response_serialization_error(
    reason: str,
) -> None:
    """Test ResponseSerializationError."""
    error = ResponseSerializationError(reason)

    assert isinstance(error, ResponseError)
    assert error.reason == reason
    assert (
        str(error)
        == (
            f"Response serialization failed: "
            f"{reason}."
        )
    )


def test_response_validation_error() -> None:
    """Test ResponseValidationError."""
    field = "status"
    reason = "Required"

    error = ResponseValidationError(
        field,
        reason,
    )

    assert isinstance(error, ResponseError)
    assert error.field == field
    assert error.reason == reason
    assert (
        str(error)
        == (
            f"Response validation failed for "
            f"'{field}': {reason}."
        )
    )


def test_response_size_exceeded_error() -> None:
    """Test ResponseSizeExceededError."""
    error = ResponseSizeExceededError(
        2048,
        1024,
    )

    assert isinstance(error, ResponseError)
    assert error.size == 2048
    assert error.maximum == 1024
    assert (
        str(error)
        == (
            "Response size (2048 bytes) exceeds "
            "maximum allowed (1024 bytes)."
        )
    )


def test_response_configuration_error() -> None:
    """Test ResponseConfigurationError."""
    configuration = "content_type"

    error = ResponseConfigurationError(
        configuration,
    )

    assert isinstance(error, ResponseError)
    assert error.configuration == configuration
    assert (
        str(error)
        == (
            "Invalid response configuration: "
            f"'{configuration}'."
        )
    )