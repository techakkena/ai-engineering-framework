"""
Constants for the ai_monitoring.analyzers module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------

RUN: Final[str] = "run"
ANALYZE: Final[str] = "analyze"
GET: Final[str] = "get"
LIST: Final[str] = "list"
COMPARE: Final[str] = "compare"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    RUN,
    ANALYZE,
    GET,
    LIST,
    COMPARE,
)

# ---------------------------------------------------------------------------
# Analysis types
# ---------------------------------------------------------------------------

PERFORMANCE: Final[str] = "performance"
RESOURCE: Final[str] = "resource"
USAGE: Final[str] = "usage"
ANOMALY: Final[str] = "anomaly"

SUPPORTED_ANALYSIS_TYPES: Final[tuple[str, ...]] = (
    PERFORMANCE,
    RESOURCE,
    USAGE,
    ANOMALY,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_ANALYSIS_ID: Final[str] = "analysis_id"
METADATA_ANALYSIS_TYPE: Final[str] = "analysis_type"
METADATA_STATUS: Final[str] = "status"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_TIMESTAMP: Final[str] = "timestamp"