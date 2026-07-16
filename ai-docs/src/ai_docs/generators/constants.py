"""Constants for the ai_docs.generators module."""

from __future__ import annotations

from typing import Final

DEFAULT_GENERATOR_NAME: Final[str] = "generator"
DEFAULT_GENERATOR_TYPE: Final[str] = "markdown"
DEFAULT_ENABLED: Final[bool] = True

MARKDOWN_GENERATOR: Final[str] = "markdown"
OPENAPI_GENERATOR: Final[str] = "openapi"
HTML_GENERATOR: Final[str] = "html"
PDF_GENERATOR: Final[str] = "pdf"

SUPPORTED_GENERATOR_TYPES: Final[frozenset[str]] = frozenset(
    {
        MARKDOWN_GENERATOR,
        OPENAPI_GENERATOR,
        HTML_GENERATOR,
        PDF_GENERATOR,
    }
)

MIN_GENERATOR_NAME_LENGTH: Final[int] = 3
MAX_GENERATOR_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_ENABLED",
    "DEFAULT_GENERATOR_NAME",
    "DEFAULT_GENERATOR_TYPE",
    "MARKDOWN_GENERATOR",
    "OPENAPI_GENERATOR",
    "HTML_GENERATOR",
    "PDF_GENERATOR",
    "SUPPORTED_GENERATOR_TYPES",
    "MIN_GENERATOR_NAME_LENGTH",
    "MAX_GENERATOR_NAME_LENGTH",
    "NAME_KEY",
    "TYPE_KEY",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
]