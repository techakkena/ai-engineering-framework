"""
ai_api.authentication

Framework-independent authentication utilities for the AI API package.

This module provides reusable authentication constants, exceptions,
and helper operations that can be integrated with FastAPI, Starlette,
Quart, Litestar, Django, Flask, or any future API framework.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_api.authentication.constants import (
    AUTHORIZATION_HEADER,
    BEARER_PREFIX,
    DEFAULT_TOKEN_EXPIRATION,
    SUPPORTED_AUTH_SCHEMES,
    TOKEN_TYPE,
)
from ai_api.authentication.exceptions import (
    AuthenticationError,
    ExpiredTokenError,
    InvalidCredentialsError,
    InvalidTokenError,
    UnsupportedAuthenticationSchemeError,
)
from ai_api.authentication.operations import (
    extract_bearer_token,
    is_bearer_token,
    normalize_auth_scheme,
    validate_auth_scheme,
    validate_token,
)

__all__ = [
    # Constants
    "AUTHORIZATION_HEADER",
    "BEARER_PREFIX",
    "DEFAULT_TOKEN_EXPIRATION",
    "SUPPORTED_AUTH_SCHEMES",
    "TOKEN_TYPE",
    # Exceptions
    "AuthenticationError",
    "ExpiredTokenError",
    "InvalidCredentialsError",
    "InvalidTokenError",
    "UnsupportedAuthenticationSchemeError",
    # Operations
    "extract_bearer_token",
    "is_bearer_token",
    "normalize_auth_scheme",
    "validate_auth_scheme",
    "validate_token",
]