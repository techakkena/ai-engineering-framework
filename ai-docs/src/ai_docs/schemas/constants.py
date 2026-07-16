"""Constants for the ai_docs.schemas module."""

from __future__ import annotations

from typing import Final

DEFAULT_SCHEMA_NAME: Final[str] = "schema"
DEFAULT_SCHEMA_FORMAT: Final[str] = "json-schema"
DEFAULT_ENABLED: Final[bool] = True

JSON_SCHEMA_FORMAT: Final[str] = "json-schema"
OPENAPI_SCHEMA_FORMAT: Final[str] = "openapi"
AVRO_SCHEMA_FORMAT: Final[str] = "avro"
PROTOBUF_SCHEMA_FORMAT: Final[str] = "protobuf"

SUPPORTED_SCHEMA_FORMATS: Final[frozenset[str]] = frozenset(
    {
        JSON_SCHEMA_FORMAT,
        OPENAPI_SCHEMA_FORMAT,
        AVRO_SCHEMA_FORMAT,
        PROTOBUF_SCHEMA_FORMAT,
    }
)

MIN_SCHEMA_NAME_LENGTH: Final[int] = 3
MAX_SCHEMA_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
FORMAT_KEY: Final[str] = "format"
CONTENT_KEY: Final[str] = "content"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "AVRO_SCHEMA_FORMAT",
    "CONTENT_KEY",
    "DEFAULT_ENABLED",
    "DEFAULT_SCHEMA_FORMAT",
    "DEFAULT_SCHEMA_NAME",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "FORMAT_KEY",
    "JSON_SCHEMA_FORMAT",
    "MAX_SCHEMA_NAME_LENGTH",
    "MIN_SCHEMA_NAME_LENGTH",
    "NAME_KEY",
    "OPENAPI_SCHEMA_FORMAT",
    "PROTOBUF_SCHEMA_FORMAT",
    "SUPPORTED_SCHEMA_FORMATS",
]