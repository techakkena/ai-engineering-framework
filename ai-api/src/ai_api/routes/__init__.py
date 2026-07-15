"""
ai_api.routes

Framework-independent routing components for the AI API package.

This module provides reusable route definitions, validation utilities,
and routing operations that can be integrated with web frameworks such
as FastAPI, Starlette, Litestar, Quart, and future adapters.

The module intentionally avoids framework-specific implementations,
allowing the AI Engineering Framework to remain portable across
multiple API technologies.

Modules:
    constants:
        Route-related constants.

    exceptions:
        Custom routing exceptions.

    operations:
        Route utility functions.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_api.routes.constants import (
    DEFAULT_ROUTE_NAME,
    DEFAULT_ROUTE_PREFIX,
    DEFAULT_TAG,
    DYNAMIC_PARAMETER_PATTERN,
    MAX_ROUTE_LENGTH,
    RESERVED_ROUTE_NAMES,
)
from ai_api.routes.exceptions import (
    DuplicateRouteNameError,
    DuplicateRoutePathError,
    InvalidRouteNameError,
    InvalidRouteParameterError,
    RouteError,
)
from ai_api.routes.operations import (
    build_route_name,
    extract_route_parameters,
    is_dynamic_route,
    is_reserved_route_name,
    normalize_route_path,
    validate_route_name,
    validate_route_path,
)

__all__ = [
    # Constants
    "DEFAULT_ROUTE_NAME",
    "DEFAULT_ROUTE_PREFIX",
    "DEFAULT_TAG",
    "DYNAMIC_PARAMETER_PATTERN",
    "MAX_ROUTE_LENGTH",
    "RESERVED_ROUTE_NAMES",
    # Exceptions
    "RouteError",
    "DuplicateRouteNameError",
    "DuplicateRoutePathError",
    "InvalidRouteNameError",
    "InvalidRouteParameterError",
    # Operations
    "build_route_name",
    "extract_route_parameters",
    "is_dynamic_route",
    "is_reserved_route_name",
    "normalize_route_path",
    "validate_route_name",
    "validate_route_path",
]