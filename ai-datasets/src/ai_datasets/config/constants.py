"""
Constants for the ai_datasets.config module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Configuration operations
# ---------------------------------------------------------------------------

LOAD: Final[str] = "load"
GET: Final[str] = "get"
UPDATE: Final[str] = "update"
RESET: Final[str] = "reset"
EXPORT: Final[str] = "export"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    LOAD,
    GET,
    UPDATE,
    RESET,
    EXPORT,
)

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

DEFAULT_CONFIG_NAME: Final[str] = "default"
DEFAULT_ENCODING: Final[str] = "utf-8"
DEFAULT_INDENT: Final[int] = 4

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_CONFIG_NAME: Final[str] = "config_name"
METADATA_ENCODING: Final[str] = "encoding"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_STATUS: Final[str] = "status"