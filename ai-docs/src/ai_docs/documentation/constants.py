"""Constants for the ai_docs.documentation module."""

from __future__ import annotations

from typing import Final

DEFAULT_DOCUMENTATION_NAME: Final[str] = "documentation"
DEFAULT_DOCUMENTATION_TYPE: Final[str] = "markdown"
DEFAULT_ENABLED: Final[bool] = True

MARKDOWN_TYPE: Final[str] = "markdown"
HTML_TYPE: Final[str] = "html"
PDF_TYPE: Final[str] = "pdf"
OPENAPI_TYPE: Final[str] = "openapi"

SUPPORTED_DOCUMENTATION_TYPES: Final[frozenset[str]] = frozenset(
    {
        MARKDOWN_TYPE,
        HTML_TYPE,
        PDF_TYPE,
        OPENAPI_TYPE,
    }
)

MIN_DOCUMENTATION_NAME_LENGTH: Final[int] = 3
MAX_DOCUMENTATION_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_DOCUMENTATION_NAME",
    "DEFAULT_DOCUMENTATION_TYPE",
    "DEFAULT_ENABLED",
    "MARKDOWN_TYPE",
    "HTML_TYPE",
    "PDF_TYPE",
    "OPENAPI_TYPE",
    "SUPPORTED_DOCUMENTATION_TYPES",
    "MIN_DOCUMENTATION_NAME_LENGTH",
    "MAX_DOCUMENTATION_NAME_LENGTH",
    "NAME_KEY",
    "TYPE_KEY",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
]