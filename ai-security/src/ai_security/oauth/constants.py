"""
Constants for the OAuth module.
"""

from __future__ import annotations

DEFAULT_GRANT_TYPE: str = "client_credentials"

DEFAULT_RESPONSE_TYPE: str = "code"

DEFAULT_TOKEN_TYPE: str = "Bearer"

SUPPORTED_GRANT_TYPES: frozenset[str] = frozenset(
    {
        "authorization_code",
        "client_credentials",
        "password",
        "refresh_token",
        "device_code",
    }
)