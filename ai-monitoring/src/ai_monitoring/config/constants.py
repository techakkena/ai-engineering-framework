"""
Constants for ai_monitoring.config.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------

LOAD: Final[str] = "load"
GET: Final[str] = "get"
UPDATE: Final[str] = "update"
EXPORT: Final[str] = "export"
LIST: Final[str] = "list"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    LOAD,
    GET,
    UPDATE,
    EXPORT,
    LIST,
)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_CONFIG_NAME: Final[str] = "default"
DEFAULT_ENCODING: Final[str] = "utf-8"
DEFAULT_INDENT: Final[int] = 4

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_CONFIG_NAME: Final[str] = "config_name"
METADATA_STATUS: Final[str] = "status"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_TIMESTAMP: Final[str] = "timestamp"