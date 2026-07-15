"""
Utility operations for the ai_api.errors module.

This module provides framework-independent helper functions for
working with standardized API errors.

All functions are deterministic, side-effect free, and easily testable.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

import re
from typing import Any

from ai_api.errors.constants import (
    CLIENT_ERROR_MAX_STATUS,
    CLIENT_ERROR_MIN_STATUS,
    DEFAULT_ERROR_MESSAGE,
    ERROR_CODE_KEY,
    ERROR_DETAILS_KEY,
    ERROR_MESSAGE_KEY,
    ERROR_TYPE_KEY,
    SERVER_ERROR_MAX_STATUS,
    SERVER_ERROR_MIN_STATUS,
    SUPPORTED_ERROR_TYPES,
)
from ai_api.errors.exceptions import (
    InvalidErrorCodeError,
    InvalidErrorTypeError,
)


def normalize_error_type(error_type: str) -> str:
    """
    Normalize an error type.

    Args:
        error_type: Error type.

    Returns:
        Normalized error type.
    """
    return error_type.strip().lower()


def validate_error_type(error_type: str) -> str:
    """
    Validate an error type.

    Args:
        error_type: Error type.

    Returns:
        Validated error type.

    Raises:
        InvalidErrorTypeError:
            If the error type is unsupported.
    """
    normalized = normalize_error_type(error_type)

    if normalized not in SUPPORTED_ERROR_TYPES:
        raise InvalidErrorTypeError(error_type)

    return normalized


def validate_error_code(error_code: str) -> str:
    """
    Validate an enterprise error code.

    Args:
        error_code: Error code.

    Returns:
        Validated error code.

    Raises:
        InvalidErrorCodeError:
            If the error code is invalid.
    """
    normalized = error_code.strip().upper()

    if not re.fullmatch(r"ERR\d{4}", normalized):
        raise InvalidErrorCodeError(error_code)

    return normalized


def build_error_code(number: int) -> str:
    """
    Build an enterprise error code.

    Args:
        number: Numeric identifier.

    Returns:
        Enterprise error code.

    Raises:
        InvalidErrorCodeError:
            If the number is outside the supported range.
    """
    if number < 0 or number > 9999:
        raise InvalidErrorCodeError(str(number))

    return f"ERR{number:04d}"


def build_error_response(
    error_code: str,
    error_type: str,
    message: str = DEFAULT_ERROR_MESSAGE,
    details: Any | None = None,
) -> dict[str, Any]:
    """
    Build a standardized error response.

    Args:
        error_code: Enterprise error code.
        error_type: Error type.
        message: Error message.
        details: Optional error details.

    Returns:
        Standardized error response.
    """
    response: dict[str, Any] = {
        ERROR_CODE_KEY: validate_error_code(error_code),
        ERROR_TYPE_KEY: validate_error_type(error_type),
        ERROR_MESSAGE_KEY: message,
    }

    if details is not None:
        response[ERROR_DETAILS_KEY] = details

    return response


def is_client_error(status_code: int) -> bool:
    """
    Determine whether an HTTP status code is a client error.

    Args:
        status_code: HTTP status code.

    Returns:
        True if the status code is in the 4xx range.
    """
    return (
        CLIENT_ERROR_MIN_STATUS
        <= status_code
        <= CLIENT_ERROR_MAX_STATUS
    )


def is_server_error(status_code: int) -> bool:
    """
    Determine whether an HTTP status code is a server error.

    Args:
        status_code: HTTP status code.

    Returns:
        True if the status code is in the 5xx range.
    """
    return (
        SERVER_ERROR_MIN_STATUS
        <= status_code
        <= SERVER_ERROR_MAX_STATUS
    )


def is_supported_error_type(error_type: str) -> bool:
    """
    Determine whether an error type is supported.

    Args:
        error_type: Error type.

    Returns:
        True if supported.
    """
    return (
        normalize_error_type(error_type)
        in SUPPORTED_ERROR_TYPES
    )