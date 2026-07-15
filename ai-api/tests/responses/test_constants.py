"""
Utility operations for the ai_api.responses module.

This module provides framework-independent helper functions for
building, validating, and working with standardized API responses.

All functions are deterministic, side-effect free, and easily testable.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from typing import Any

from ai_api.responses.constants import (
    DEFAULT_ERROR_MESSAGE,
    DEFAULT_SUCCESS_MESSAGE,
    ERROR_KEY,
    ERROR_STATUS,
    MESSAGE_KEY,
    STATUS_KEY,
    SUCCESS_STATUS,
    SUPPORTED_CONTENT_TYPES,
)
from ai_api.responses.exceptions import (
    InvalidContentTypeError,
    InvalidResponseError,
)


def normalize_content_type(content_type: str) -> str:
    """
    Normalize a content type.

    Args:
        content_type: HTTP content type.

    Returns:
        Normalized content type.
    """
    return content_type.strip().lower()


def validate_content_type(content_type: str) -> str:
    """
    Validate a content type.

    Args:
        content_type: HTTP content type.

    Returns:
        Validated content type.

    Raises:
        InvalidContentTypeError:
            If the content type is unsupported.
    """
    normalized = normalize_content_type(content_type)

    if normalized not in SUPPORTED_CONTENT_TYPES:
        raise InvalidContentTypeError(content_type)

    return normalized


def build_success_response(
    data: Any,
    message: str = DEFAULT_SUCCESS_MESSAGE,
) -> dict[str, Any]:
    """
    Build a standardized success response.

    Args:
        data: Response payload.
        message: Success message.

    Returns:
        Success response dictionary.
    """
    return {
        STATUS_KEY: SUCCESS_STATUS,
        MESSAGE_KEY: message,
        "data": data,
    }


def build_error_response(
    message: str = DEFAULT_ERROR_MESSAGE,
    error: Any | None = None,
) -> dict[str, Any]:
    """
    Build a standardized error response.

    Args:
        message: Error message.
        error: Optional error details.

    Returns:
        Error response dictionary.
    """
    response = {
        STATUS_KEY: ERROR_STATUS,
        MESSAGE_KEY: message,
    }

    if error is not None:
        response[ERROR_KEY] = error

    return response


def validate_response(
    response: dict[str, Any],
) -> dict[str, Any]:
    """
    Validate a response object.

    Args:
        response: Response dictionary.

    Returns:
        Validated response.

    Raises:
        InvalidResponseError:
            If required fields are missing.
    """
    if STATUS_KEY not in response:
        raise InvalidResponseError("missing status")

    if MESSAGE_KEY not in response:
        raise InvalidResponseError("missing message")

    return response


def is_supported_content_type(
    content_type: str,
) -> bool:
    """
    Determine whether a content type is supported.

    Args:
        content_type: HTTP content type.

    Returns:
        True if supported.
    """
    return (
        normalize_content_type(content_type)
        in SUPPORTED_CONTENT_TYPES
    )


def is_success_response(
    response: dict[str, Any],
) -> bool:
    """
    Determine whether a response represents success.

    Args:
        response: Response dictionary.

    Returns:
        True if the response status is success.
    """
    return (
        response.get(STATUS_KEY)
        == SUCCESS_STATUS
    )


def is_error_response(
    response: dict[str, Any],
) -> bool:
    """
    Determine whether a response represents an error.

    Args:
        response: Response dictionary.

    Returns:
        True if the response status is error.
    """
    return (
        response.get(STATUS_KEY)
        == ERROR_STATUS
    )