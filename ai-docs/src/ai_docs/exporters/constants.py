"""Constants for the ai_docs.exporters module."""

from __future__ import annotations

from typing import Final

DEFAULT_EXPORT_NAME: Final[str] = "export"
DEFAULT_EXPORT_FORMAT: Final[str] = "markdown"
DEFAULT_ENABLED: Final[bool] = True

MARKDOWN_FORMAT: Final[str] = "markdown"
HTML_FORMAT: Final[str] = "html"
PDF_FORMAT: Final[str] = "pdf"
JSON_FORMAT: Final[str] = "json"

SUPPORTED_EXPORT_FORMATS: Final[frozenset[str]] = frozenset(
    {
        MARKDOWN_FORMAT,
        HTML_FORMAT,
        PDF_FORMAT,
        JSON_FORMAT,
    }
)

MIN_EXPORT_NAME_LENGTH: Final[int] = 3
MAX_EXPORT_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
FORMAT_KEY: Final[str] = "format"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_ENABLED",
    "DEFAULT_EXPORT_FORMAT",
    "DEFAULT_EXPORT_NAME",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "FORMAT_KEY",
    "HTML_FORMAT",
    "JSON_FORMAT",
    "MARKDOWN_FORMAT",
    "MAX_EXPORT_NAME_LENGTH",
    "MIN_EXPORT_NAME_LENGTH",
    "NAME_KEY",
    "PDF_FORMAT",
    "SUPPORTED_EXPORT_FORMATS",
]