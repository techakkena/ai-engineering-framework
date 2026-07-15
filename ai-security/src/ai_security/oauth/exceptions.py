"""
Exceptions for the OAuth module.
"""

from __future__ import annotations


class OAuthError(Exception):
    """Base exception for OAuth operations."""


class OAuthConfigurationError(OAuthError):
    """Raised when OAuth configuration is invalid."""


class OAuthAuthenticationError(OAuthError):
    """Raised when authentication fails."""


class OAuthAuthorizationError(OAuthError):
    """Raised when authorization fails."""


class OAuthTokenError(OAuthError):
    """Raised when token operations fail."""