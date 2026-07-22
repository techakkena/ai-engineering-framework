"""
Constants for the ai_monitoring.health module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Health operations
# ---------------------------------------------------------------------------

CHECK: Final[str] = "check"
RUN: Final[str] = "run"
GET: Final[str] = "get"
LIST: Final[str] = "list"
REGISTER: Final[str] = "register"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    CHECK,
    RUN,
    GET,
    LIST,
    REGISTER,
)

# ---------------------------------------------------------------------------
# Health status
# ---------------------------------------------------------------------------

HEALTHY: Final[str] = "healthy"
DEGRADED: Final[str] = "degraded"
UNHEALTHY: Final[str] = "unhealthy"
UNKNOWN: Final[str] = "unknown"

SUPPORTED_STATUSES: Final[tuple[str, ...]] = (
    HEALTHY,
    DEGRADED,
    UNHEALTHY,
    UNKNOWN,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_CHECK_NAME: Final[str] = "check_name"
METADATA_STATUS: Final[str] = "status"
METADATA_TIMESTAMP: Final[str] = "timestamp"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_MESSAGE: Final[str] = "message"