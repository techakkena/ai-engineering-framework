"""
Constants for the ai_datasets.cache module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Cache operations
# ---------------------------------------------------------------------------

CACHE: Final[str] = "cache"
GET: Final[str] = "get"
INVALIDATE: Final[str] = "invalidate"
CLEAR: Final[str] = "clear"
STATISTICS: Final[str] = "statistics"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    CACHE,
    GET,
    INVALIDATE,
    CLEAR,
    STATISTICS,
)

# ---------------------------------------------------------------------------
# Cache defaults
# ---------------------------------------------------------------------------

DEFAULT_TTL: Final[int] = 3600
DEFAULT_MAX_ENTRIES: Final[int] = 1000

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_CACHE_KEY: Final[str] = "cache_key"
METADATA_TTL: Final[str] = "ttl"
METADATA_CACHE_SIZE: Final[str] = "cache_size"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_STATUS: Final[str] = "status"