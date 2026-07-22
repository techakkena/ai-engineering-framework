"""
Constants for the ai_monitoring.logging module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Logging operations
# ---------------------------------------------------------------------------

LOG: Final[str] = "log"
EVENT: Final[str] = "event"
GET: Final[str] = "get"
LIST: Final[str] = "list"
CLEAR: Final[str] = "clear"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    LOG,
    EVENT,
    GET,
    LIST,
    CLEAR,
)

# ---------------------------------------------------------------------------
# Log levels
# ---------------------------------------------------------------------------

DEBUG: Final[str] = "DEBUG"
INFO: Final[str] = "INFO"
WARNING: Final[str] = "WARNING"
ERROR: Final[str] = "ERROR"
CRITICAL: Final[str] = "CRITICAL"

SUPPORTED_LEVELS: Final[tuple[str, ...]] = (
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_LOG_ID: Final[str] = "log_id"
METADATA_LEVEL: Final[str] = "level"
METADATA_TIMESTAMP: Final[str] = "timestamp"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_STATUS: Final[str] = "status"