"""
Constants for the ai_monitoring.telemetry module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------

COLLECT: Final[str] = "collect"
GET: Final[str] = "get"
LIST: Final[str] = "list"
EXPORT: Final[str] = "export"
RESET: Final[str] = "reset"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    COLLECT,
    GET,
    LIST,
    EXPORT,
    RESET,
)

# ---------------------------------------------------------------------------
# Telemetry types
# ---------------------------------------------------------------------------

METRIC: Final[str] = "metric"
TRACE: Final[str] = "trace"
LOG: Final[str] = "log"
EVENT: Final[str] = "event"

SUPPORTED_TYPES: Final[tuple[str, ...]] = (
    METRIC,
    TRACE,
    LOG,
    EVENT,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_TELEMETRY_ID: Final[str] = "telemetry_id"
METADATA_TYPE: Final[str] = "type"
METADATA_TIMESTAMP: Final[str] = "timestamp"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_STATUS: Final[str] = "status"