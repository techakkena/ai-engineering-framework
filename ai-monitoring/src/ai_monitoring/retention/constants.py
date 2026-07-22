"""
Constants for the ai_monitoring.retention module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------

CREATE: Final[str] = "create"
APPLY: Final[str] = "apply"
GET: Final[str] = "get"
LIST: Final[str] = "list"
DELETE: Final[str] = "delete"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    CREATE,
    APPLY,
    GET,
    LIST,
    DELETE,
)

# ---------------------------------------------------------------------------
# Policy types
# ---------------------------------------------------------------------------

TIME_BASED: Final[str] = "time_based"
SIZE_BASED: Final[str] = "size_based"
HYBRID: Final[str] = "hybrid"

SUPPORTED_POLICY_TYPES: Final[tuple[str, ...]] = (
    TIME_BASED,
    SIZE_BASED,
    HYBRID,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_POLICY_ID: Final[str] = "policy_id"
METADATA_POLICY_TYPE: Final[str] = "policy_type"
METADATA_STATUS: Final[str] = "status"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_TIMESTAMP: Final[str] = "timestamp"