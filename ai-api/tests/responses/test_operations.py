"""
Unit tests for ai_api.responses.operations.
"""

from __future__ import annotations

import pytest

from ai_api.responses.constants import (
    DEFAULT_ERROR_MESSAGE,
    DEFAULT_SUCCESS_MESSAGE,
    ERROR_KEY,
    ERROR_STATUS,
    MESSAGE_KEY,
    STATUS_KEY,
    SUCCESS_STATUS,
)
from ai_api.responses.exceptions import (
    InvalidContentTypeError,
    InvalidResponseError,
)
from ai_api.responses.operations import (
    build_error_response,
    build_success_response,
    is_error_response,
    is_success_response,
    is_supported_content_type,
    normalize_content_type,
    validate_content_type,
    validate_response,
)


# ============================================================================
# normalize_content_type
# ============================================================================


@pytest.mark.parametrize(
    ("content_type", "expected"),
    [
        ("Application/JSON", "application/json"),
        (" TEXT/PLAIN ", "text/plain"),
        ("Application/XML", "application/xml"),
    ],
)
def test_normalize_content_type(
    content_type: str,
    expected: str,
) -> None:
    """Test content type normalization."""
    assert normalize_content_type(content_type) == expected


# ============================================================================
# validate_content_type
# ============================================================================


@pytest.mark.parametrize(
    "content_type",
    [
        "application/json",
        "text/plain",
        "text/html",
        "application/xml",
        "text/csv",
        "application/octet-stream",
    ],
)
def test_validate_content_type(
    content_type: str,
) -> None:
    """Test supported content types."""
    assert validate_content_type(content_type) == content_type


@pytest.mark.parametrize(
    "content_type",
    [
        "",
        "application/pdf",
        "image/png",
        "application/yaml",
    ],
)
def test_validate_content_type_invalid(
    content_type: str,
) -> None:
    """Unsupported content types should raise."""
    with pytest.raises(
        InvalidContentTypeError,
    ):
        validate_content_type(content_type)


# ============================================================================
# build_success_response
# ============================================================================


def test_build_success_response_default() -> None:
    """Test building a default success response."""
    data = {"id": 1}

    response = build_success_response(data)

    assert response[STATUS_KEY] == SUCCESS_STATUS
    assert response[MESSAGE_KEY] == DEFAULT_SUCCESS_MESSAGE
    assert response["data"] == data


def test_build_success_response_custom_message() -> None:
    """Test building a success response with a custom message."""
    response = build_success_response(
        {"name": "Alice"},
        "Operation completed.",
    )

    assert response[STATUS_KEY] == SUCCESS_STATUS
    assert response[MESSAGE_KEY] == "Operation completed."
    assert response["data"] == {"name": "Alice"}


# ============================================================================
# build_error_response
# ============================================================================


def test_build_error_response_default() -> None:
    """Test building a default error response."""
    response = build_error_response()

    assert response[STATUS_KEY] == ERROR_STATUS
    assert response[MESSAGE_KEY] == DEFAULT_ERROR_MESSAGE
    assert ERROR_KEY not in response


def test_build_error_response_with_error() -> None:
    """Test building an error response with details."""
    response = build_error_response(
        "Validation failed.",
        {"field": "email"},
    )

    assert response[STATUS_KEY] == ERROR_STATUS
    assert response[MESSAGE_KEY] == "Validation failed."
    assert response[ERROR_KEY] == {"field": "email"}


# ============================================================================
# validate_response
# ============================================================================


def test_validate_response_success() -> None:
    """Test validating a valid response."""
    response = {
        STATUS_KEY: SUCCESS_STATUS,
        MESSAGE_KEY: "OK",
    }

    assert validate_response(response) == response


def test_validate_response_missing_status() -> None:
    """Missing status should raise."""
    with pytest.raises(
        InvalidResponseError,
    ):
        validate_response(
            {
                MESSAGE_KEY: "OK",
            }
        )


def test_validate_response_missing_message() -> None:
    """Missing message should raise."""
    with pytest.raises(
        InvalidResponseError,
    ):
        validate_response(
            {
                STATUS_KEY: SUCCESS_STATUS,
            }
        )


# ============================================================================
# is_supported_content_type
# ============================================================================


@pytest.mark.parametrize(
    ("content_type", "expected"),
    [
        ("application/json", True),
        ("text/plain", True),
        ("application/xml", True),
        ("application/pdf", False),
        ("image/png", False),
    ],
)
def test_is_supported_content_type(
    content_type: str,
    expected: bool,
) -> None:
    """Test supported content type detection."""
    assert (
        is_supported_content_type(content_type)
        is expected
    )


# ============================================================================
# is_success_response
# ============================================================================


def test_is_success_response() -> None:
    """Test success response detection."""
    response = build_success_response(
        {"id": 1},
    )

    assert is_success_response(response) is True
    assert is_error_response(response) is False


# ============================================================================
# is_error_response
# ============================================================================


def test_is_error_response() -> None:
    """Test error response detection."""
    response = build_error_response(
        "Failed",
    )

    assert is_error_response(response) is True
    assert is_success_response(response) is False