"""
Constants for the ai_api.authentication module.

This module defines immutable constants used throughout the
authentication components of the AI API package.

The constants are framework-independent and provide sensible defaults
for authentication schemes, token handling, headers, and expiration
settings.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# HTTP Headers
# ============================================================================

AUTHORIZATION_HEADER: Final[str] = "Authorization"

API_KEY_HEADER: Final[str] = "X-API-Key"

TOKEN_HEADER: Final[str] = "X-Access-Token"

# ============================================================================
# Authentication Schemes
# ============================================================================

BEARER_PREFIX: Final[str] = "Bearer"

BASIC_PREFIX: Final[str] = "Basic"

DIGEST_PREFIX: Final[str] = "Digest"

TOKEN_TYPE: Final[str] = "Bearer"

# ============================================================================
# Supported Authentication Schemes
# ============================================================================

SUPPORTED_AUTH_SCHEMES: Final[frozenset[str]] = frozenset(
    {
        "bearer",
        "basic",
        "apikey",
        "oauth2",
        "jwt",
        "session",
    }
)

# ============================================================================
# Token Configuration
# ============================================================================

DEFAULT_TOKEN_EXPIRATION: Final[int] = 3600

DEFAULT_REFRESH_TOKEN_EXPIRATION: Final[int] = 86400

DEFAULT_CLOCK_SKEW: Final[int] = 60

# ============================================================================
# Token Claims
# ============================================================================

SUBJECT_CLAIM: Final[str] = "sub"

ISSUER_CLAIM: Final[str] = "iss"

AUDIENCE_CLAIM: Final[str] = "aud"

ISSUED_AT_CLAIM: Final[str] = "iat"

EXPIRES_AT_CLAIM: Final[str] = "exp"

NOT_BEFORE_CLAIM: Final[str] = "nbf"

JWT_ID_CLAIM: Final[str] = "jti"

# ============================================================================
# API Keys
# ============================================================================

API_KEY_PREFIX: Final[str] = "ak"

MIN_API_KEY_LENGTH: Final[int] = 32

MAX_API_KEY_LENGTH: Final[int] = 256

# ============================================================================
# Password Policy
# ============================================================================

MIN_PASSWORD_LENGTH: Final[int] = 8

MAX_PASSWORD_LENGTH: Final[int] = 128

# ============================================================================
# Username Policy
# ============================================================================

MIN_USERNAME_LENGTH: Final[int] = 3

MAX_USERNAME_LENGTH: Final[int] = 64