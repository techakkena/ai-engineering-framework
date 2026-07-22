"""
Constants for the ai_monitoring.dashboards module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------

CREATE: Final[str] = "create"
GET: Final[str] = "get"
UPDATE: Final[str] = "update"
DELETE: Final[str] = "delete"
LIST: Final[str] = "list"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    CREATE,
    GET,
    UPDATE,
    DELETE,
    LIST,
)

# ---------------------------------------------------------------------------
# Dashboard types
# ---------------------------------------------------------------------------

SYSTEM: Final[str] = "system"
APPLICATION: Final[str] = "application"
BUSINESS: Final[str] = "business"
CUSTOM: Final[str] = "custom"

SUPPORTED_DASHBOARD_TYPES: Final[tuple[str, ...]] = (
    SYSTEM,
    APPLICATION,
    BUSINESS,
    CUSTOM,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_DASHBOARD_ID: Final[str] = "dashboard_id"
METADATA_NAME: Final[str] = "name"
METADATA_TYPE: Final[str] = "type"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_STATUS: Final[str] = "status"