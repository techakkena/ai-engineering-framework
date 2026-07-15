"""
ai_api.responses

Framework-independent response utilities for the AI API package.

This module provides reusable response constants, exceptions, and
helper operations for constructing standardized API responses.

The module is intentionally framework-independent and can be
integrated with FastAPI, Starlette, Quart, Litestar, Flask,
Django, or any future API framework.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_api.responses.constants import (
    DEFAULT_CONTENT_TYPE,
    DEFAULT_ERROR_MESSAGE,
    DEFAULT_SUCCESS_MESSAGE,
    DEFAULT_VERSION,
    JSON_CONTENT_TYPE,
    SUPPORTED_CONTENT_TYPES,
)
from ai_api.responses.exceptions import (
    InvalidContentTypeError,
    InvalidResponseError,
    ResponseError,
    ResponseSerializationError,
    UnsupportedResponseTypeError,
)
from ai_api.responses.operations import (
    build_error_response,
    build_success_response,
    is_supported_content_type,
    normalize_content_type,
    validate_content_type,
    validate_response,
)

__all__ = [
    # Constants
    "DEFAULT_CONTENT_TYPE",
    "DEFAULT_ERROR_MESSAGE",
    "DEFAULT_SUCCESS_MESSAGE",
    "DEFAULT_VERSION",
    "JSON_CONTENT_TYPE",
    "SUPPORTED_CONTENT_TYPES",
    # Exceptions
    "ResponseError",
    "InvalidContentTypeError",
    "InvalidResponseError",
    "ResponseSerializationError",
    "UnsupportedResponseTypeError",
    # Operations
    "build_error_response",
    "build_success_response",
    "is_supported_content_type",
    "normalize_content_type",
    "validate_content_type",
    "validate_response",
]