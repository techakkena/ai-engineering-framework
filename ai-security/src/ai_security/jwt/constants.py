"""
Constants for the JWT module.
"""

from __future__ import annotations

DEFAULT_ALGORITHM: str = "HS256"

DEFAULT_EXPIRATION_SECONDS: int = 3600

DEFAULT_ISSUER: str = "ai-engineering-framework"

DEFAULT_AUDIENCE: str = "ai-framework"

SUPPORTED_ALGORITHMS: frozenset[str] = frozenset(
    {
        "HS256",
        "HS384",
        "HS512",
        "RS256",
        "RS384",
        "RS512",
        "ES256",
        "ES384",
        "ES512",
    }
)