"""Constants for the ai_cloud.authentication module."""

from __future__ import annotations

from typing import Final

DEFAULT_AUTHENTICATION_NAME: Final[str] = "authentication"
DEFAULT_AUTHENTICATION_TYPE: Final[str] = "api_key"
DEFAULT_ENABLED: Final[bool] = True

API_KEY_AUTH: Final[str] = "api_key"
OAUTH2_AUTH: Final[str] = "oauth2"
JWT_AUTH: Final[str] = "jwt"
IAM_AUTH: Final[str] = "iam"

SUPPORTED_AUTHENTICATION_TYPES: Final[frozenset[str]] = frozenset(
    {
        API_KEY_AUTH,
        OAUTH2_AUTH,
        JWT_AUTH,
        IAM_AUTH,
    }
)

MIN_AUTHENTICATION_NAME_LENGTH: Final[int] = 1
MAX_AUTHENTICATION_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
CREDENTIAL_KEY: Final[str] = "credential"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "API_KEY_AUTH",
    "CREDENTIAL_KEY",
    "DEFAULT_AUTHENTICATION_NAME",
    "DEFAULT_AUTHENTICATION_TYPE",
    "DEFAULT_ENABLED",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "IAM_AUTH",
    "JWT_AUTH",
    "MAX_AUTHENTICATION_NAME_LENGTH",
    "MIN_AUTHENTICATION_NAME_LENGTH",
    "NAME_KEY",
    "OAUTH2_AUTH",
    "SUPPORTED_AUTHENTICATION_TYPES",
    "TYPE_KEY",
]