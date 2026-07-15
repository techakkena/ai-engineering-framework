"""
Utility operations for the ai_api.routes module.

This module provides framework-independent helper functions for
working with API routes, route names, and route parameters.

All functions are deterministic, side-effect free, and easily testable.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

import re

from ai_api.routes.constants import (
    DYNAMIC_PARAMETER_PATTERN,
    MAX_ROUTE_LENGTH,
    RESERVED_ROUTE_NAMES,
)
from ai_api.routes.exceptions import (
    InvalidRouteNameError,
    InvalidRouteParameterError,
    InvalidRoutePathError,
    ReservedRouteNameError,
    RouteLengthExceededError,
)


def normalize_route_path(path: str) -> str:
    """
    Normalize a route path.

    Args:
        path: Route path.

    Returns:
        Normalized route path.
    """
    if not path:
        return "/"

    path = "/" + path.strip("/")

    while "//" in path:
        path = path.replace("//", "/")

    if path != "/" and path.endswith("/"):
        path = path[:-1]

    return path


def validate_route_path(path: str) -> str:
    """
    Validate a route path.

    Args:
        path: Route path.

    Returns:
        Normalized route path.

    Raises:
        InvalidRoutePathError:
            If the route path is invalid.

        RouteLengthExceededError:
            If the route exceeds the maximum length.
    """
    path = normalize_route_path(path)

    if len(path) > MAX_ROUTE_LENGTH:
        raise RouteLengthExceededError(
            len(path),
            MAX_ROUTE_LENGTH,
        )

    if " " in path:
        raise InvalidRoutePathError(path)

    return path


def validate_route_name(name: str) -> str:
    """
    Validate a route name.

    Args:
        name: Route name.

    Returns:
        Normalized route name.

    Raises:
        InvalidRouteNameError
        ReservedRouteNameError
    """
    name = name.strip().lower()

    if not name:
        raise InvalidRouteNameError(name)

    if not re.fullmatch(r"[a-z][a-z0-9_]*", name):
        raise InvalidRouteNameError(name)

    if name in RESERVED_ROUTE_NAMES:
        raise ReservedRouteNameError(name)

    return name


def build_route_name(method: str, path: str) -> str:
    """
    Build a deterministic route name.

    Example:
        GET /users/profile

    becomes

        get_users_profile
    """
    path = normalize_route_path(path)

    cleaned = (
        path.strip("/")
        .replace("/", "_")
        .replace("-", "_")
    )

    method = method.lower()

    if not cleaned:
        return method

    return f"{method}_{cleaned}"


def extract_route_parameters(path: str) -> list[str]:
    """
    Extract route parameters.

    Example:
        /users/{user_id}/posts/{post_id}

    returns

        ["user_id", "post_id"]
    """
    return re.findall(
        DYNAMIC_PARAMETER_PATTERN,
        path,
    )


def is_dynamic_route(path: str) -> bool:
    """
    Determine whether a route contains parameters.
    """
    return bool(
        extract_route_parameters(path)
    )


def is_reserved_route_name(name: str) -> bool:
    """
    Determine whether a route name is reserved.
    """
    return name.strip().lower() in RESERVED_ROUTE_NAMES


def validate_route_parameter(parameter: str) -> str:
    """
    Validate a route parameter.

    Args:
        parameter: Route parameter.

    Returns:
        Validated parameter.

    Raises:
        InvalidRouteParameterError
    """
    parameter = parameter.strip()

    if not parameter:
        raise InvalidRouteParameterError(parameter)

    if not re.fullmatch(
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        parameter,
    ):
        raise InvalidRouteParameterError(parameter)

    return parameter