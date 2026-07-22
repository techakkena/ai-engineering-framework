"""
Constants for the ai_monitoring.alerts module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Alert operations
# ---------------------------------------------------------------------------

CREATE: Final[str] = "create"
ACKNOWLEDGE: Final[str] = "acknowledge"
RESOLVE: Final[str] = "resolve"
GET: Final[str] = "get"
LIST: Final[str] = "list"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    CREATE,
    ACKNOWLEDGE,
    RESOLVE,
    GET,
    LIST,
)

# ---------------------------------------------------------------------------
# Alert severity
# ---------------------------------------------------------------------------

INFO: Final[str] = "info"
WARNING: Final[str] = "warning"
ERROR: Final[str] = "error"
CRITICAL: Final[str] = "critical"

SUPPORTED_SEVERITIES: Final[tuple[str, ...]] = (
    INFO,
    WARNING,
    ERROR,
    CRITICAL,
)

# ---------------------------------------------------------------------------
# Alert status
# ---------------------------------------------------------------------------

OPEN: Final[str] = "open"
ACKNOWLEDGED: Final[str] = "acknowledged"
RESOLVED: Final[str] = "resolved"

SUPPORTED_STATUSES: Final[tuple[str, ...]] = (
    OPEN,
    ACKNOWLEDGED,
    RESOLVED,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_ALERT_ID: Final[str] = "alert_id"
METADATA_SEVERITY: Final[str] = "severity"
METADATA_STATUS: Final[str] = "status"
METADATA_TIMESTAMP: Final[str] = "timestamp"
METADATA_DURATION: Final[str] = "duration_ms"