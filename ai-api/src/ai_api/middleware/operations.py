"""
Utility operations for the ai_api.middleware module.

This module provides framework-independent helper functions for
middleware name normalization, validation, type validation, and
priority handling.

All functions are deterministic, side-effect free, and easily testable.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from ai_api.middleware.constants import (
    MAX_MIDDLEWARE_NAME_LENGTH,
    MIDDLEWARE_PRIORITY,
    SUPPORTED_MIDDLEWARE_TYPES,
)
from ai_api.middleware.exceptions import (
    InvalidMiddlewareConfigurationError,
    InvalidMiddlewareTypeError,
    MiddlewarePriorityError,
)


def normalize_middleware_name(name: str) -> str:
    """
    Normalize a middleware name.

    Args:
        name: Middleware name.

    Returns:
        Normalized middleware name.
    """
    return name.strip().lower().replace("-", "_").replace(" ", "_")


def validate_middleware_name(name: str) -> str:
    """
    Validate a middleware name.

    Args:
        name: Middleware name.

    Returns:
        Validated middleware name.

    Raises:
        InvalidMiddlewareConfigurationError:
            If the middleware name is invalid.
    """
    normalized = normalize_middleware_name(name)

    if not normalized:
        raise InvalidMiddlewareConfigurationError(name)

    if len(normalized) > MAX_MIDDLEWARE_NAME_LENGTH:
        raise InvalidMiddlewareConfigurationError(name)

    if not normalized.replace("_", "").isalnum():
        raise InvalidMiddlewareConfigurationError(name)

    return normalized


def validate_middleware_type(middleware_type: str) -> str:
    """
    Validate a middleware type.

    Args:
        middleware_type: Middleware type.

    Returns:
        Normalized middleware type.

    Raises:
        InvalidMiddlewareTypeError:
            If the middleware type is unsupported.
    """
    normalized = middleware_type.strip().lower()

    if normalized not in SUPPORTED_MIDDLEWARE_TYPES:
        raise InvalidMiddlewareTypeError(middleware_type)

    return normalized


def get_middleware_priority(name: str) -> int:
    """
    Get the execution priority for a middleware.

    Args:
        name: Middleware name.

    Returns:
        Middleware priority.

    Raises:
        MiddlewarePriorityError:
            If no priority exists.
    """
    normalized = normalize_middleware_name(name)

    try:
        return MIDDLEWARE_PRIORITY[normalized]
    except KeyError as exc:
        raise MiddlewarePriorityError(-1) from exc


def build_middleware_name(
    middleware_type: str,
    name: str,
) -> str:
    """
    Build a deterministic middleware name.

    Args:
        middleware_type: Middleware type.
        name: Middleware name.

    Returns:
        Middleware identifier.
    """
    middleware_type = validate_middleware_type(middleware_type)
    name = validate_middleware_name(name)

    return f"{middleware_type}_{name}"


def is_supported_middleware(
    middleware_type: str,
) -> bool:
    """
    Determine whether a middleware type is supported.

    Args:
        middleware_type: Middleware type.

    Returns:
        True if supported.
    """
    return (
        middleware_type.strip().lower()
        in SUPPORTED_MIDDLEWARE_TYPES
    )


def sort_middlewares(
    middleware_names: list[str],
) -> list[str]:
    """
    Sort middleware names by execution priority.

    Args:
        middleware_names: List of middleware names.

    Returns:
        Sorted middleware names.
    """
    return sorted(
        middleware_names,
        key=get_middleware_priority,
    )


def validate_configuration(
    configuration: dict[str, object],
) -> dict[str, object]:
    """
    Validate middleware configuration.

    Args:
        configuration: Middleware configuration.

    Returns:
        Validated configuration.

    Raises:
        InvalidMiddlewareConfigurationError:
            If the configuration is empty.
    """
    if not configuration:
        raise InvalidMiddlewareConfigurationError(
            "configuration"
        )

    return configuration