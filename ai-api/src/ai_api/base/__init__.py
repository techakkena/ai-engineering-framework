"""
ai_api.base

Core abstractions, constants, exceptions, and utility operations for the
AI API package.

This module provides framework-agnostic building blocks used throughout
the ``ai_api`` package, including:

- API constants
- Base exceptions
- Route and version utilities
- HTTP method validation

These components are designed to be reusable across multiple web
frameworks such as FastAPI, Starlette, and future integrations.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_api.base.constants import (
    DEFAULT_API_VERSION,
    DEFAULT_CONTENT_TYPE,
    DEFAULT_DOCS_PATH,
    DEFAULT_OPENAPI_PATH,
    DEFAULT_PREFIX,
    DEFAULT_REDOC_PATH,
    DEFAULT_TIMEOUT,
    JSON_MEDIA_TYPE,
    SUPPORTED_HTTP_METHODS,
)
from ai_api.base.exceptions import (
    APIError,
    ConfigurationError,
    InvalidAPIVersionError,
    InvalidRouteError,
    RouteAlreadyExistsError,
    UnsupportedHTTPMethodError,
)
from ai_api.base.operations import (
    build_endpoint_name,
    ensure_leading_slash,
    is_valid_api_version,
    join_route,
    normalize_path,
    normalize_version,
    remove_duplicate_slashes,
    validate_http_method,
)

__all__ = [
    # Constants
    "DEFAULT_API_VERSION",
    "DEFAULT_CONTENT_TYPE",
    "DEFAULT_DOCS_PATH",
    "DEFAULT_OPENAPI_PATH",
    "DEFAULT_PREFIX",
    "DEFAULT_REDOC_PATH",
    "DEFAULT_TIMEOUT",
    "JSON_MEDIA_TYPE",
    "SUPPORTED_HTTP_METHODS",
    # Exceptions
    "APIError",
    "ConfigurationError",
    "InvalidAPIVersionError",
    "InvalidRouteError",
    "RouteAlreadyExistsError",
    "UnsupportedHTTPMethodError",
    # Operations
    "build_endpoint_name",
    "ensure_leading_slash",
    "is_valid_api_version",
    "join_route",
    "normalize_path",
    "normalize_version",
    "remove_duplicate_slashes",
    "validate_http_method",
]
