"""
Constants for the ai_monitoring.collectors module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------

REGISTER: Final[str] = "register"
COLLECT: Final[str] = "collect"
GET: Final[str] = "get"
LIST: Final[str] = "list"
REMOVE: Final[str] = "remove"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    REGISTER,
    COLLECT,
    GET,
    LIST,
    REMOVE,
)

# ---------------------------------------------------------------------------
# Collector Types
# ---------------------------------------------------------------------------

SYSTEM: Final[str] = "system"
APPLICATION: Final[str] = "application"
CUSTOM: Final[str] = "custom"
REMOTE: Final[str] = "remote"

SUPPORTED_COLLECTORS: Final[tuple[str, ...]] = (
    SYSTEM,
    APPLICATION,
    CUSTOM,
    REMOTE,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_COLLECTOR_ID: Final[str] = "collector_id"
METADATA_COLLECTOR_TYPE: Final[str] = "collector_type"
METADATA_STATUS: Final[str] = "status"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_TIMESTAMP: Final[str] = "timestamp"