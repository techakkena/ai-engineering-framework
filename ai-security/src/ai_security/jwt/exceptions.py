"""
Exceptions for the JWT module.
"""

from __future__ import annotations


class JWTError(Exception):
    """Base exception for JWT operations."""


class JWTConfigurationError(JWTError):
    """Raised when JWT configuration is invalid."""


class JWTEncodeError(JWTError):
    """Raised when token encoding fails."""


class JWTDecodeError(JWTError):
    """Raised when token decoding fails."""


class JWTValidationError(JWTError):
    """Raised when JWT validation fails."""