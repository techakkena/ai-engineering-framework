"""
Constants for ai_security.authentication.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Defaults
# ============================================================================

DEFAULT_AUTH_PROVIDER: Final[str] = "local"

DEFAULT_AUTH_SCHEME: Final[str] = "bearer"

DEFAULT_TOKEN_EXPIRY: Final[int] = 3600

# ============================================================================
# Providers
# ============================================================================

LOCAL: Final[str] = "local"

JWT: Final[str] = "jwt"

OAUTH2: Final[str] = "oauth2"

OPENID_CONNECT: Final[str] = "openid-connect"

LDAP: Final[str] = "ldap"

ACTIVE_DIRECTORY: Final[str] = "active-directory"

SUPPORTED_AUTH_PROVIDERS: Final[
    frozenset[str]
] = frozenset(
    {
        LOCAL,
        JWT,
        OAUTH2,
        OPENID_CONNECT,
        LDAP,
        ACTIVE_DIRECTORY,
    }
)

# ============================================================================
# Authentication Schemes
# ============================================================================

BEARER: Final[str] = "bearer"

BASIC: Final[str] = "basic"

API_KEY: Final[str] = "api-key"

SUPPORTED_AUTH_SCHEMES: Final[
    frozenset[str]
] = frozenset(
    {
        BEARER,
        BASIC,
        API_KEY,
    }
)

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_TIMEOUT: Final[int] = 30

DEFAULT_RETRIES: Final[int] = 3