"""
Constants for the ai_datasets.exporters module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Export formats
# ---------------------------------------------------------------------------

EXPORT_CSV: Final[str] = "csv"
EXPORT_JSON: Final[str] = "json"
EXPORT_PARQUET: Final[str] = "parquet"
EXPORT_EXCEL: Final[str] = "excel"

SUPPORTED_EXPORT_FORMATS: Final[tuple[str, ...]] = (
    EXPORT_CSV,
    EXPORT_JSON,
    EXPORT_PARQUET,
    EXPORT_EXCEL,
)

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

DEFAULT_ENCODING: Final[str] = "utf-8"
DEFAULT_DELIMITER: Final[str] = ","
DEFAULT_OVERWRITE: Final[bool] = False

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_FORMAT: Final[str] = "format"
METADATA_RECORD_COUNT: Final[str] = "record_count"
METADATA_OUTPUT_PATH: Final[str] = "output_path"
METADATA_DURATION: Final[str] = "duration_ms"