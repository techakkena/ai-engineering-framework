"""
ai_security.authorization

Framework-independent authorization utilities.

This module provides reusable constants, exceptions, and helper
operations for authorization.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_security.authorization.constants import (
    DEFAULT_AUTHORIZATION_PROVIDER,
    DEFAULT_POLICY,
    DEFAULT_ROLE,
    SUPPORTED_AUTHORIZATION_PROVIDERS,
)
from ai_security.authorization.exceptions import (
    AuthorizationConfigurationError,
    AuthorizationError,
    AuthorizationValidationError,
    InvalidAuthorizationProviderError,
)
from ai_security.authorization.operations import (
    build_authorization_id,
    is_supported_authorization_provider,
    normalize_authorization_provider,
    validate_authorization_id,
    validate_authorization_provider,
)

__all__ = [
    "DEFAULT_AUTHORIZATION_PROVIDER",
    "DEFAULT_POLICY",
    "DEFAULT_ROLE",
    "SUPPORTED_AUTHORIZATION_PROVIDERS",
    "AuthorizationError",
    "InvalidAuthorizationProviderError",
    "AuthorizationConfigurationError",
    "AuthorizationValidationError",
    "build_authorization_id",
    "is_supported_authorization_provider",
    "normalize_authorization_provider",
    "validate_authorization_id",
    "validate_authorization_provider",
]