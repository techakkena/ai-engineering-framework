"""
Constants for the ai_monitoring.metrics module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Metric operations
# ---------------------------------------------------------------------------

COLLECT: Final[str] = "collect"
RECORD: Final[str] = "record"
GET: Final[str] = "get"
LIST: Final[str] = "list"
RESET: Final[str] = "reset"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    COLLECT,
    RECORD,
    GET,
    LIST,
    RESET,
)

# ---------------------------------------------------------------------------
# Metric types
# ---------------------------------------------------------------------------

COUNTER: Final[str] = "counter"
GAUGE: Final[str] = "gauge"
HISTOGRAM: Final[str] = "histogram"
SUMMARY: Final[str] = "summary"

SUPPORTED_METRIC_TYPES: Final[tuple[str, ...]] = (
    COUNTER,
    GAUGE,
    HISTOGRAM,
    SUMMARY,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_NAME: Final[str] = "metric_name"
METADATA_TYPE: Final[str] = "metric_type"
METADATA_VALUE: Final[str] = "value"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_STATUS: Final[str] = "status"