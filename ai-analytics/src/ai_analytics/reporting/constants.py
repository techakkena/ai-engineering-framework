"""Constants for the ai_analytics.reporting module."""

from __future__ import annotations

from typing import Final

DEFAULT_REPORT_NAME: Final[str] = "report"
DEFAULT_REPORT_FORMAT: Final[str] = "json"
DEFAULT_ENABLED: Final[bool] = True

JSON_FORMAT: Final[str] = "json"
CSV_FORMAT: Final[str] = "csv"
HTML_FORMAT: Final[str] = "html"
PDF_FORMAT: Final[str] = "pdf"

SUPPORTED_REPORT_FORMATS: Final[frozenset[str]] = frozenset(
    {
        JSON_FORMAT,
        CSV_FORMAT,
        HTML_FORMAT,
        PDF_FORMAT,
    }
)

MIN_REPORT_NAME_LENGTH: Final[int] = 1
MAX_REPORT_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
FORMAT_KEY: Final[str] = "format"
TITLE_KEY: Final[str] = "title"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "CSV_FORMAT",
    "DEFAULT_ENABLED",
    "DEFAULT_REPORT_FORMAT",
    "DEFAULT_REPORT_NAME",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "FORMAT_KEY",
    "HTML_FORMAT",
    "JSON_FORMAT",
    "MAX_REPORT_NAME_LENGTH",
    "MIN_REPORT_NAME_LENGTH",
    "NAME_KEY",
    "PDF_FORMAT",
    "SUPPORTED_REPORT_FORMATS",
    "TITLE_KEY",
]