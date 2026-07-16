"""
Constants for the ai_datasets.parsers module.

This module defines framework-independent constants used by dataset
parsing operations.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Supported parser types
# ---------------------------------------------------------------------------

PARSER_CSV: Final[str] = "csv"
PARSER_JSON: Final[str] = "json"
PARSER_JSONL: Final[str] = "jsonl"
PARSER_PARQUET: Final[str] = "parquet"
PARSER_XML: Final[str] = "xml"

SUPPORTED_PARSERS: Final[tuple[str, ...]] = (
    PARSER_CSV,
    PARSER_JSON,
    PARSER_JSONL,
    PARSER_PARQUET,
    PARSER_XML,
)

# ---------------------------------------------------------------------------
# Parsing defaults
# ---------------------------------------------------------------------------

DEFAULT_DELIMITER: Final[str] = ","
DEFAULT_ENCODING: Final[str] = "utf-8"
DEFAULT_BATCH_SIZE: Final[int] = 1000

# ---------------------------------------------------------------------------
# JSON parsing
# ---------------------------------------------------------------------------

DEFAULT_INDENT: Final[int] = 2
DEFAULT_STRICT_MODE: Final[bool] = True

# ---------------------------------------------------------------------------
# XML parsing
# ---------------------------------------------------------------------------

DEFAULT_XML_ROOT: Final[str] = "root"

# ---------------------------------------------------------------------------
# Metadata keys
# ---------------------------------------------------------------------------

METADATA_SOURCE: Final[str] = "source"
METADATA_PARSER: Final[str] = "parser"
METADATA_RECORD_COUNT: Final[str] = "record_count"
METADATA_ENCODING: Final[str] = "encoding"
METADATA_DURATION: Final[str] = "duration_ms"