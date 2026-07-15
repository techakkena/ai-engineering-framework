"""
ai_api.errors

Framework-independent error handling utilities for the AI API package.

This module provides reusable constants, exceptions, and helper
operations for standardized API error handling.

The module is intentionally framework-independent and can be
integrated with FastAPI, Starlette, Quart, Litestar, Flask,
Django, or any future API framework.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_api.errors.constants import (
    DEFAULT_ERROR_CODE,
    DEFAULT_ERROR_MESSAGE,
    DEFAULT_ERROR_TYPE,
    INTERNAL_ERROR_CODE,
    NOT_FOUND_ERROR_CODE,
    VALIDATION_ERROR_CODE,
)
from ai_api.errors.exceptions import (
    ErrorConfigurationError,
    ErrorHandlingError,
    ErrorMappingError,
    InvalidErrorCodeError,
    InvalidErrorTypeError,
)
from ai_api.errors.operations import (
    build_error_code,
    build_error_response,
    is_client_error,
    is_server_error,
    normalize_error_type,
    validate_error_code,
    validate_error_type,
)

__all__ = [
    # Constants
    "DEFAULT_ERROR_CODE",
    "DEFAULT_ERROR_MESSAGE",
    "DEFAULT_ERROR_TYPE",
    "INTERNAL_ERROR_CODE",
    "NOT_FOUND_ERROR_CODE",
    "VALIDATION_ERROR_CODE",
    # Exceptions
    "ErrorConfigurationError",
    "ErrorHandlingError",
    "ErrorMappingError",
    "InvalidErrorCodeError",
    "InvalidErrorTypeError",
    # Operations
    "build_error_code",
    "build_error_response",
    "is_client_error",
    "is_server_error",
    "normalize_error_type",
    "validate_error_code",
    "validate_error_type",
]