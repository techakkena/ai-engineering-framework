"""
Constants for the ai_datasets.loaders module.

This module defines framework-independent constants used by dataset
loading operations.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Supported loader types
# ---------------------------------------------------------------------------

LOADER_CSV: Final[str] = "csv"
LOADER_JSON: Final[str] = "json"
LOADER_PARQUET: Final[str] = "parquet"
LOADER_TEXT: Final[str] = "text"
LOADER_DATABASE: Final[str] = "database"

SUPPORTED_LOADERS: Final[tuple[str, ...]] = (
    LOADER_CSV,
    LOADER_JSON,
    LOADER_PARQUET,
    LOADER_TEXT,
    LOADER_DATABASE,
)

# ---------------------------------------------------------------------------
# File extensions
# ---------------------------------------------------------------------------

CSV_EXTENSION: Final[str] = ".csv"
JSON_EXTENSION: Final[str] = ".json"
PARQUET_EXTENSION: Final[str] = ".parquet"
TEXT_EXTENSION: Final[str] = ".txt"

# ---------------------------------------------------------------------------
# Loading defaults
# ---------------------------------------------------------------------------

DEFAULT_DELIMITER: Final[str] = ","
DEFAULT_ENCODING: Final[str] = "utf-8"
DEFAULT_BATCH_SIZE: Final[int] = 1000
DEFAULT_HAS_HEADER: Final[bool] = True

# ---------------------------------------------------------------------------
# Database defaults
# ---------------------------------------------------------------------------

DEFAULT_FETCH_SIZE: Final[int] = 1000
DEFAULT_CONNECTION_TIMEOUT: Final[int] = 30

# ---------------------------------------------------------------------------
# Metadata keys
# ---------------------------------------------------------------------------

METADATA_SOURCE: Final[str] = "source"
METADATA_LOADER: Final[str] = "loader"
METADATA_RECORD_COUNT: Final[str] = "record_count"
METADATA_ENCODING: Final[str] = "encoding"
METADATA_DURATION: Final[str] = "duration_ms"