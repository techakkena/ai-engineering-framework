"""
ai_security.authentication

Framework-independent authentication utilities.

This module provides reusable constants, exceptions, and helper
operations for authentication.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_security.authentication.constants import (
    DEFAULT_AUTH_PROVIDER,
    DEFAULT_AUTH_SCHEME,
    DEFAULT_TOKEN_EXPIRY,
    SUPPORTED_AUTH_PROVIDERS,
)
from ai_security.authentication.exceptions import (
    AuthenticationConfigurationError,
    AuthenticationError,
    AuthenticationValidationError,
    InvalidAuthenticationProviderError,
)
from ai_security.authentication.operations import (
    build_authentication_id,
    is_supported_authentication_provider,
    normalize_authentication_provider,
    validate_authentication_id,
    validate_authentication_provider,
)

__all__ = [
    "DEFAULT_AUTH_PROVIDER",
    "DEFAULT_AUTH_SCHEME",
    "DEFAULT_TOKEN_EXPIRY",
    "SUPPORTED_AUTH_PROVIDERS",
    "AuthenticationError",
    "InvalidAuthenticationProviderError",
    "AuthenticationConfigurationError",
    "AuthenticationValidationError",
    "build_authentication_id",
    "is_supported_authentication_provider",
    "normalize_authentication_provider",
    "validate_authentication_id",
    "validate_authentication_provider",
]