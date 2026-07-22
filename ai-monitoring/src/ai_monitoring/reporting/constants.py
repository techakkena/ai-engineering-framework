"""
Constants for the ai_monitoring.reporting module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------

CREATE: Final[str] = "create"
EXPORT: Final[str] = "export"
GET: Final[str] = "get"
LIST: Final[str] = "list"
DELETE: Final[str] = "delete"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    CREATE,
    EXPORT,
    GET,
    LIST,
    DELETE,
)

# ---------------------------------------------------------------------------
# Report Types
# ---------------------------------------------------------------------------

SUMMARY: Final[str] = "summary"
DETAILED: Final[str] = "detailed"
DAILY: Final[str] = "daily"
MONTHLY: Final[str] = "monthly"

SUPPORTED_REPORT_TYPES: Final[tuple[str, ...]] = (
    SUMMARY,
    DETAILED,
    DAILY,
    MONTHLY,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_REPORT_ID: Final[str] = "report_id"
METADATA_REPORT_TYPE: Final[str] = "report_type"
METADATA_STATUS: Final[str] = "status"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_TIMESTAMP: Final[str] = "timestamp"