"""Constants for the ai_analytics.export module."""

from __future__ import annotations

from typing import Final

DEFAULT_EXPORT_NAME: Final[str] = "export"
DEFAULT_EXPORT_FORMAT: Final[str] = "json"
DEFAULT_ENABLED: Final[bool] = True

JSON_FORMAT: Final[str] = "json"
CSV_FORMAT: Final[str] = "csv"
PARQUET_FORMAT: Final[str] = "parquet"
EXCEL_FORMAT: Final[str] = "xlsx"

SUPPORTED_EXPORT_FORMATS: Final[frozenset[str]] = frozenset(
    {
        JSON_FORMAT,
        CSV_FORMAT,
        PARQUET_FORMAT,
        EXCEL_FORMAT,
    }
)

MIN_EXPORT_NAME_LENGTH: Final[int] = 1
MAX_EXPORT_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
FORMAT_KEY: Final[str] = "format"
DESTINATION_KEY: Final[str] = "destination"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "CSV_FORMAT",
    "DEFAULT_ENABLED",
    "DEFAULT_EXPORT_FORMAT",
    "DEFAULT_EXPORT_NAME",
    "DESCRIPTION_KEY",
    "DESTINATION_KEY",
    "ENABLED_KEY",
    "EXCEL_FORMAT",
    "FORMAT_KEY",
    "JSON_FORMAT",
    "MAX_EXPORT_NAME_LENGTH",
    "MIN_EXPORT_NAME_LENGTH",
    "NAME_KEY",
    "PARQUET_FORMAT",
    "SUPPORTED_EXPORT_FORMATS",
]