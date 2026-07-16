"""Constants for the ai_cloud.secrets module."""

from __future__ import annotations

from typing import Final

DEFAULT_SECRET_NAME: Final[str] = "secret"
DEFAULT_SECRET_TYPE: Final[str] = "api_key"
DEFAULT_ENABLED: Final[bool] = True

API_KEY_TYPE: Final[str] = "api_key"
TOKEN_TYPE: Final[str] = "token"
PASSWORD_TYPE: Final[str] = "password"
CERTIFICATE_TYPE: Final[str] = "certificate"

SUPPORTED_SECRET_TYPES: Final[frozenset[str]] = frozenset(
    {
        API_KEY_TYPE,
        TOKEN_TYPE,
        PASSWORD_TYPE,
        CERTIFICATE_TYPE,
    }
)

MIN_SECRET_NAME_LENGTH: Final[int] = 1
MAX_SECRET_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
VALUE_KEY: Final[str] = "value"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "API_KEY_TYPE",
    "CERTIFICATE_TYPE",
    "DEFAULT_ENABLED",
    "DEFAULT_SECRET_NAME",
    "DEFAULT_SECRET_TYPE",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "MAX_SECRET_NAME_LENGTH",
    "MIN_SECRET_NAME_LENGTH",
    "NAME_KEY",
    "PASSWORD_TYPE",
    "SUPPORTED_SECRET_TYPES",
    "TOKEN_TYPE",
    "TYPE_KEY",
    "VALUE_KEY",
]