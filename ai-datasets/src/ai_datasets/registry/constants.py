"""
Constants for the ai_datasets.registry module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Registry operations
# ---------------------------------------------------------------------------

REGISTER: Final[str] = "register"
UPDATE: Final[str] = "update"
DELETE: Final[str] = "delete"
GET: Final[str] = "get"
LIST: Final[str] = "list"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    REGISTER,
    UPDATE,
    DELETE,
    GET,
    LIST,
)

# ---------------------------------------------------------------------------
# Dataset lifecycle
# ---------------------------------------------------------------------------

STATUS_ACTIVE: Final[str] = "active"
STATUS_INACTIVE: Final[str] = "inactive"
STATUS_DEPRECATED: Final[str] = "deprecated"

SUPPORTED_STATUSES: Final[tuple[str, ...]] = (
    STATUS_ACTIVE,
    STATUS_INACTIVE,
    STATUS_DEPRECATED,
)

# ---------------------------------------------------------------------------
# Metadata keys
# ---------------------------------------------------------------------------

METADATA_DATASET_ID: Final[str] = "dataset_id"
METADATA_VERSION: Final[str] = "version"
METADATA_OWNER: Final[str] = "owner"
METADATA_STATUS: Final[str] = "status"
METADATA_DURATION: Final[str] = "duration_ms"