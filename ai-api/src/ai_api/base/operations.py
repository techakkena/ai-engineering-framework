"""
Utility operations for the ai_api.base module.

This module provides framework-independent helper functions for working
with API paths, versions, endpoint names, and HTTP methods.

All functions are deterministic, side-effect free, and easily testable.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

import re

from ai_api.base.constants import SUPPORTED_HTTP_METHODS
from ai_api.base.exceptions import (
    InvalidAPIVersionError,
    UnsupportedHTTPMethodError,
)


def ensure_leading_slash(path: str) -> str:
    """
    Ensure a path starts with a leading slash.

    Args:
        path: Input path.

    Returns:
        Normalized path with a leading slash.
    """
    if not path:
        return "/"

    return path if path.startswith("/") else f"/{path}"


def remove_duplicate_slashes(path: str) -> str:
    """
    Remove duplicate slashes from a path.

    Args:
        path: Input path.

    Returns:
        Path with duplicate slashes removed.
    """
    if not path:
        return "/"

    normalized = re.sub(r"/+", "/", path)

    return normalized or "/"


def normalize_path(path: str) -> str:
    """
    Normalize an API path.

    Normalization includes:

    - Ensure leading slash
    - Remove duplicate slashes
    - Remove trailing slash (except root)

    Args:
        path: API path.

    Returns:
        Normalized path.
    """
    normalized = ensure_leading_slash(path)
    normalized = remove_duplicate_slashes(normalized)

    if normalized != "/" and normalized.endswith("/"):
        normalized = normalized[:-1]

    return normalized


def join_route(*parts: str) -> str:
    """
    Join route parts into a normalized API path.

    Args:
        *parts: Route components.

    Returns:
        Joined route.
    """
    cleaned = [part.strip("/") for part in parts if part and part.strip("/")]

    if not cleaned:
        return "/"

    return normalize_path("/".join(cleaned))


def normalize_version(version: str) -> str:
    """
    Normalize an API version.

    Examples:
        "1" -> "v1"
        "v1" -> "v1"
        "V2" -> "v2"

    Args:
        version: Version string.

    Returns:
        Normalized version.

    Raises:
        InvalidAPIVersionError:
            If version is empty.
    """
    version = version.strip().lower()

    if not version:
        raise InvalidAPIVersionError()

    if version.startswith("v"):
        return version

    return f"v{version}"


def is_valid_api_version(version: str) -> bool:
    """
    Determine whether an API version is valid.

    Valid examples:

    - v1
    - v2
    - v10

    Args:
        version: Version string.

    Returns:
        True if valid.
    """
    return bool(re.fullmatch(r"v\d+", normalize_version(version)))


def validate_http_method(method: str) -> str:
    """
    Validate an HTTP method.

    Args:
        method: HTTP method.

    Returns:
        Uppercase HTTP method.

    Raises:
        UnsupportedHTTPMethodError:
            If the method is not supported.
    """
    normalized = method.strip().upper()

    if normalized not in SUPPORTED_HTTP_METHODS:
        raise UnsupportedHTTPMethodError(normalized)

    return normalized


def build_endpoint_name(method: str, path: str) -> str:
    """
    Build a deterministic endpoint name.

    Example:
        GET + /users/profile

    becomes

        get_users_profile

    Args:
        method: HTTP method.
        path: Route path.

    Returns:
        Endpoint name.
    """
    normalized_method = validate_http_method(method).lower()

    normalized_path = (
        normalize_path(path).strip("/").replace("/", "_").replace("-", "_")
    )

    if not normalized_path:
        return normalized_method

    return f"{normalized_method}_{normalized_path}"
