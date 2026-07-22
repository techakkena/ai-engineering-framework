"""
Constants for ai_monitoring.utils.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------

BUILD: Final[str] = "build"
FORMAT: Final[str] = "format"
GENERATE: Final[str] = "generate"
VALIDATE: Final[str] = "validate"
TIMESTAMP: Final[str] = "timestamp"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    BUILD,
    FORMAT,
    GENERATE,
    VALIDATE,
    TIMESTAMP,
)

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

DEFAULT_PREFIX: Final[str] = "monitor"
DEFAULT_SEPARATOR: Final[str] = "-"
DEFAULT_TIME_UNIT: Final[str] = "ms"

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_ID: Final[str] = "id"
METADATA_CREATED_AT: Final[str] = "created_at"
METADATA_STATUS: Final[str] = "status"
METADATA_DURATION: Final[str] = "duration_ms"