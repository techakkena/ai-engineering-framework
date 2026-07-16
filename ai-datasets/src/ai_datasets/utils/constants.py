"""
Constants for the ai_datasets.utils module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Utility operations
# ---------------------------------------------------------------------------

STATISTICS: Final[str] = "statistics"
SUMMARY: Final[str] = "summary"
SCHEMA: Final[str] = "schema"
VALIDATE_DATASET: Final[str] = "validate_dataset"
VALIDATE_RECORD: Final[str] = "validate_record"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    STATISTICS,
    SUMMARY,
    SCHEMA,
    VALIDATE_DATASET,
    VALIDATE_RECORD,
)

# ---------------------------------------------------------------------------
# Metadata keys
# ---------------------------------------------------------------------------

METADATA_RECORD_COUNT: Final[str] = "record_count"
METADATA_FIELD_COUNT: Final[str] = "field_count"
METADATA_SCHEMA: Final[str] = "schema"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_STATUS: Final[str] = "status"