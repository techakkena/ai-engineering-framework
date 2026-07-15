"""
OAuth utilities for the AI Engineering Framework.

This package provides framework-independent abstractions for OAuth 2.0
authentication and authorization workflows.
"""

from ai_security.oauth.constants import (
    DEFAULT_GRANT_TYPE,
    DEFAULT_RESPONSE_TYPE,
    DEFAULT_TOKEN_TYPE,
    SUPPORTED_GRANT_TYPES,
)
from ai_security.oauth.exceptions import (
    OAuthAuthenticationError,
    OAuthAuthorizationError,
    OAuthConfigurationError,
    OAuthError,
    OAuthTokenError,
)
from ai_security.oauth.operations import (
    OAuthClient,
    OAuthService,
    OAuthToken,
)

__all__ = [
    "DEFAULT_GRANT_TYPE",
    "DEFAULT_RESPONSE_TYPE",
    "DEFAULT_TOKEN_TYPE",
    "SUPPORTED_GRANT_TYPES",
    "OAuthError",
    "OAuthConfigurationError",
    "OAuthAuthenticationError",
    "OAuthAuthorizationError",
    "OAuthTokenError",
    "OAuthClient",
    "OAuthToken",
    "OAuthService",
]