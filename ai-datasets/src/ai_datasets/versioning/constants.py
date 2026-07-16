"""
Constants for the ai_datasets.versioning module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Version operations
# ---------------------------------------------------------------------------

CREATE: Final[str] = "create"
GET: Final[str] = "get"
LIST: Final[str] = "list"
COMPARE: Final[str] = "compare"
ROLLBACK: Final[str] = "rollback"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    CREATE,
    GET,
    LIST,
    COMPARE,
    ROLLBACK,
)

# ---------------------------------------------------------------------------
# Version status
# ---------------------------------------------------------------------------

STATUS_ACTIVE: Final[str] = "active"
STATUS_ARCHIVED: Final[str] = "archived"
STATUS_DEPRECATED: Final[str] = "deprecated"

SUPPORTED_STATUSES: Final[tuple[str, ...]] = (
    STATUS_ACTIVE,
    STATUS_ARCHIVED,
    STATUS_DEPRECATED,
)

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

DEFAULT_VERSION: Final[str] = "1.0.0"

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_VERSION: Final[str] = "version"
METADATA_PREVIOUS_VERSION: Final[str] = "previous_version"
METADATA_DATASET_ID: Final[str] = "dataset_id"
METADATA_STATUS: Final[str] = "status"
METADATA_DURATION: Final[str] = "duration_ms"