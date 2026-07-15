"""
Unit tests for ai_api.errors.operations.
"""

from __future__ import annotations

import pytest

from ai_api.errors.constants import (
    DEFAULT_ERROR_MESSAGE,
    ERROR_CODE_KEY,
    ERROR_DETAILS_KEY,
    ERROR_MESSAGE_KEY,
    ERROR_TYPE_KEY,
)
from ai_api.errors.exceptions import (
    InvalidErrorCodeError,
    InvalidErrorTypeError,
)
from ai_api.errors.operations import (
    build_error_code,
    build_error_response,
    is_client_error,
    is_server_error,
    is_supported_error_type,
    normalize_error_type,
    validate_error_code,
    validate_error_type,
)


# ============================================================================
# normalize_error_type
# ============================================================================


@pytest.mark.parametrize(
    ("error_type", "expected"),
    [
        ("Validation_Error", "validation_error"),
        (" INTERNAL_ERROR ", "internal_error"),
        ("Authentication_Error", "authentication_error"),
        ("Authorization_Error", "authorization_error"),
    ],
)
def test_normalize_error_type(
    error_type: str,
    expected: str,
) -> None:
    """Test error type normalization."""
    assert normalize_error_type(error_type) == expected


# ============================================================================
# validate_error_type
# ============================================================================


@pytest.mark.parametrize(
    "error_type",
    [
        "validation_error",
        "authentication_error",
        "authorization_error",
        "not_found_error",
        "conflict_error",
        "rate_limit_error",
        "internal_error",
    ],
)
def test_validate_error_type(
    error_type: str,
) -> None:
    """Test supported error types."""
    assert validate_error_type(error_type) == error_type


@pytest.mark.parametrize(
    "error_type",
    [
        "",
        "database_error",
        "network_error",
        "custom_error",
    ],
)
def test_validate_error_type_invalid(
    error_type: str,
) -> None:
    """Unsupported error types should raise."""
    with pytest.raises(
        InvalidErrorTypeError,
    ):
        validate_error_type(error_type)


# ============================================================================
# validate_error_code
# ============================================================================


@pytest.mark.parametrize(
    "error_code",
    [
        "ERR0000",
        "ERR1000",
        "ERR5000",
        "err1234",
    ],
)
def test_validate_error_code(
    error_code: str,
) -> None:
    """Test valid error codes."""
    assert (
        validate_error_code(error_code)
        == error_code.upper()
    )


@pytest.mark.parametrize(
    "error_code",
    [
        "",
        "ERR",
        "ABC1000",
        "ERR123",
        "ERR12345",
    ],
)
def test_validate_error_code_invalid(
    error_code: str,
) -> None:
    """Invalid error codes should raise."""
    with pytest.raises(
        InvalidErrorCodeError,
    ):
        validate_error_code(error_code)


# ============================================================================
# build_error_code
# ============================================================================


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (0, "ERR0000"),
        (1, "ERR0001"),
        (404, "ERR0404"),
        (1000, "ERR1000"),
        (9999, "ERR9999"),
    ],
)
def test_build_error_code(
    number: int,
    expected: str,
) -> None:
    """Test enterprise error code generation."""
    assert build_error_code(number) == expected


@pytest.mark.parametrize(
    "number",
    [
        -1,
        10000,
    ],
)
def test_build_error_code_invalid(
    number: int,
) -> None:
    """Invalid code numbers should raise."""
    with pytest.raises(
        InvalidErrorCodeError,
    ):
        build_error_code(number)


# ============================================================================
# build_error_response
# ============================================================================


def test_build_error_response_default() -> None:
    """Test default error response."""
    response = build_error_response(
        "ERR1000",
        "validation_error",
    )

    assert response[ERROR_CODE_KEY] == "ERR1000"
    assert (
        response[ERROR_TYPE_KEY]
        == "validation_error"
    )
    assert (
        response[ERROR_MESSAGE_KEY]
        == DEFAULT_ERROR_MESSAGE
    )
    assert ERROR_DETAILS_KEY not in response


def test_build_error_response_with_details() -> None:
    """Test error response with details."""
    details = {"field": "email"}

    response = build_error_response(
        "ERR1000",
        "validation_error",
        "Validation failed.",
        details,
    )

    assert response[ERROR_CODE_KEY] == "ERR1000"
    assert (
        response[ERROR_TYPE_KEY]
        == "validation_error"
    )
    assert (
        response[ERROR_MESSAGE_KEY]
        == "Validation failed."
    )
    assert response[ERROR_DETAILS_KEY] == details


# ============================================================================
# is_client_error
# ============================================================================


@pytest.mark.parametrize(
    ("status_code", "expected"),
    [
        (399, False),
        (400, True),
        (404, True),
        (499, True),
        (500, False),
    ],
)
def test_is_client_error(
    status_code: int,
    expected: bool,
) -> None:
    """Test client error detection."""
    assert (
        is_client_error(status_code)
        is expected
    )


# ============================================================================
# is_server_error
# ============================================================================


@pytest.mark.parametrize(
    ("status_code", "expected"),
    [
        (499, False),
        (500, True),
        (503, True),
        (599, True),
        (600, False),
    ],
)
def test_is_server_error(
    status_code: int,
    expected: bool,
) -> None:
    """Test server error detection."""
    assert (
        is_server_error(status_code)
        is expected
    )


# ============================================================================
# is_supported_error_type
# ============================================================================


@pytest.mark.parametrize(
    ("error_type", "expected"),
    [
        ("validation_error", True),
        ("authentication_error", True),
        ("authorization_error", True),
        ("internal_error", True),
        ("database_error", False),
        ("network_error", False),
    ],
)
def test_is_supported_error_type(
    error_type: str,
    expected: bool,
) -> None:
    """Test supported error type detection."""
    assert (
        is_supported_error_type(error_type)
        is expected
    )