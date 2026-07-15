"""
JWT utilities for ai_security.

This package provides framework-independent JSON Web Token (JWT)
operations for token generation, validation, decoding, and claims
management.
"""

from ai_security.jwt.constants import (
    DEFAULT_ALGORITHM,
    DEFAULT_AUDIENCE,
    DEFAULT_EXPIRATION_SECONDS,
    DEFAULT_ISSUER,
    SUPPORTED_ALGORITHMS,
)
from ai_security.jwt.exceptions import (
    JWTConfigurationError,
    JWTDecodeError,
    JWTEncodeError,
    JWTError,
    JWTValidationError,
)
from ai_security.jwt.operations import (
    JWTClaims,
    JWTService,
)

__all__ = [
    "DEFAULT_ALGORITHM",
    "DEFAULT_AUDIENCE",
    "DEFAULT_EXPIRATION_SECONDS",
    "DEFAULT_ISSUER",
    "SUPPORTED_ALGORITHMS",
    "JWTError",
    "JWTConfigurationError",
    "JWTEncodeError",
    "JWTDecodeError",
    "JWTValidationError",
    "JWTClaims",
    "JWTService",
]