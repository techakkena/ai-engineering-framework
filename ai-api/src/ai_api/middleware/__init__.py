"""
ai_api.middleware

Framework-independent middleware utilities for the AI API package.

This module provides reusable middleware abstractions, constants,
exceptions, and helper operations that can be adapted to different
Python web frameworks such as FastAPI, Starlette, Quart, and Litestar.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_api.middleware.constants import (
    DEFAULT_CORRELATION_ID_HEADER,
    DEFAULT_REQUEST_ID_HEADER,
    DEFAULT_TIMEOUT,
    MIDDLEWARE_PRIORITY,
    SUPPORTED_MIDDLEWARE_TYPES,
)
from ai_api.middleware.exceptions import (
    DuplicateMiddlewareError,
    InvalidMiddlewareConfigurationError,
    InvalidMiddlewareTypeError,
    MiddlewareError,
)
from ai_api.middleware.operations import (
    build_middleware_name,
    normalize_middleware_name,
    validate_middleware_name,
    validate_middleware_type,
)

__all__ = [
    "DEFAULT_CORRELATION_ID_HEADER",
    "DEFAULT_REQUEST_ID_HEADER",
    "DEFAULT_TIMEOUT",
    "MIDDLEWARE_PRIORITY",
    "SUPPORTED_MIDDLEWARE_TYPES",
    "MiddlewareError",
    "DuplicateMiddlewareError",
    "InvalidMiddlewareConfigurationError",
    "InvalidMiddlewareTypeError",
    "build_middleware_name",
    "normalize_middleware_name",
    "validate_middleware_name",
    "validate_middleware_type",
]