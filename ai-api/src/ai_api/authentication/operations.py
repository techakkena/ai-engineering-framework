"""
Utility operations for the ai_api.authentication module.

This module provides framework-independent helper functions for
authentication scheme validation, bearer token extraction, and
token validation.

All functions are deterministic, side-effect free, and easily testable.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from ai_api.authentication.constants import (
    BEARER_PREFIX,
    SUPPORTED_AUTH_SCHEMES,
)
from ai_api.authentication.exceptions import (
    InvalidTokenError,
    MissingAuthorizationHeaderError,
    UnsupportedAuthenticationSchemeError,
)


def normalize_auth_scheme(scheme: str) -> str:
    """
    Normalize an authentication scheme.

    Args:
        scheme: Authentication scheme.

    Returns:
        Normalized authentication scheme.
    """
    return scheme.strip().lower()


def validate_auth_scheme(scheme: str) -> str:
    """
    Validate an authentication scheme.

    Args:
        scheme: Authentication scheme.

    Returns:
        Normalized authentication scheme.

    Raises:
        UnsupportedAuthenticationSchemeError:
            If the scheme is unsupported.
    """
    normalized = normalize_auth_scheme(scheme)

    if normalized not in SUPPORTED_AUTH_SCHEMES:
        raise UnsupportedAuthenticationSchemeError(scheme)

    return normalized


def is_bearer_token(authorization: str) -> bool:
    """
    Determine whether an Authorization header contains a Bearer token.

    Args:
        authorization: Authorization header.

    Returns:
        True if the header contains a Bearer token.
    """
    return authorization.strip().startswith(f"{BEARER_PREFIX} ")


def extract_bearer_token(authorization: str) -> str:
    """
    Extract a Bearer token from an Authorization header.

    Args:
        authorization: Authorization header.

    Returns:
        Extracted Bearer token.

    Raises:
        MissingAuthorizationHeaderError:
            If the header is empty.

        InvalidTokenError:
            If the Bearer token is invalid.
    """
    authorization = authorization.strip()

    if not authorization:
        raise MissingAuthorizationHeaderError()

    if not is_bearer_token(authorization):
        raise InvalidTokenError()

    token = authorization[len(BEARER_PREFIX) + 1 :].strip()

    if not token:
        raise InvalidTokenError()

    return token


def validate_token(token: str) -> str:
    """
    Validate a token.

    This function performs basic validation only.
    Cryptographic verification should be performed by
    framework-specific adapters.

    Args:
        token: Authentication token.

    Returns:
        Validated token.

    Raises:
        InvalidTokenError:
            If the token is invalid.
    """
    token = token.strip()

    if not token:
        raise InvalidTokenError()

    if len(token) < 8:
        raise InvalidTokenError()

    return token


def build_authorization_header(token: str) -> str:
    """
    Build a Bearer Authorization header.

    Args:
        token: Authentication token.

    Returns:
        Authorization header.
    """
    token = validate_token(token)

    return f"{BEARER_PREFIX} {token}"


def split_authorization_header(
    authorization: str,
) -> tuple[str, str]:
    """
    Split an Authorization header into scheme and credentials.

    Args:
        authorization: Authorization header.

    Returns:
        Tuple containing the authentication scheme and credentials.

    Raises:
        MissingAuthorizationHeaderError:
            If the header is empty.

        InvalidTokenError:
            If the header format is invalid.
    """
    authorization = authorization.strip()

    if not authorization:
        raise MissingAuthorizationHeaderError()

    parts = authorization.split(maxsplit=1)

    if len(parts) != 2:
        raise InvalidTokenError()

    return parts[0], parts[1]


def is_supported_auth_scheme(scheme: str) -> bool:
    """
    Determine whether an authentication scheme is supported.

    Args:
        scheme: Authentication scheme.

    Returns:
        True if supported.
    """
    return normalize_auth_scheme(scheme) in SUPPORTED_AUTH_SCHEMES