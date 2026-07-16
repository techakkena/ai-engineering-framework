"""Constants for the ai_docs.openapi module."""

from __future__ import annotations

from typing import Final

DEFAULT_OPENAPI_NAME: Final[str] = "openapi"
DEFAULT_OPENAPI_VERSION: Final[str] = "3.1.0"
DEFAULT_ENABLED: Final[bool] = True

OPENAPI_30: Final[str] = "3.0.3"
OPENAPI_31: Final[str] = "3.1.0"

SUPPORTED_OPENAPI_VERSIONS: Final[frozenset[str]] = frozenset(
    {
        OPENAPI_30,
        OPENAPI_31,
    }
)

MIN_OPENAPI_NAME_LENGTH: Final[int] = 3
MAX_OPENAPI_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
VERSION_KEY: Final[str] = "version"
TITLE_KEY: Final[str] = "title"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_ENABLED",
    "DEFAULT_OPENAPI_NAME",
    "DEFAULT_OPENAPI_VERSION",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "MAX_OPENAPI_NAME_LENGTH",
    "MIN_OPENAPI_NAME_LENGTH",
    "NAME_KEY",
    "OPENAPI_30",
    "OPENAPI_31",
    "SUPPORTED_OPENAPI_VERSIONS",
    "TITLE_KEY",
    "VERSION_KEY",
]