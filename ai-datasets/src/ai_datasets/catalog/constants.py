"""
Constants for the ai_datasets.catalog module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Catalog operations
# ---------------------------------------------------------------------------

REGISTER: Final[str] = "register"
UNREGISTER: Final[str] = "unregister"
GET: Final[str] = "get"
LIST: Final[str] = "list"
SEARCH: Final[str] = "search"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    REGISTER,
    UNREGISTER,
    GET,
    LIST,
    SEARCH,
)

# ---------------------------------------------------------------------------
# Dataset status
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
# Metadata
# ---------------------------------------------------------------------------

METADATA_DATASET_ID: Final[str] = "dataset_id"
METADATA_VERSION: Final[str] = "version"
METADATA_OWNER: Final[str] = "owner"
METADATA_STATUS: Final[str] = "status"
METADATA_DURATION: Final[str] = "duration_ms"