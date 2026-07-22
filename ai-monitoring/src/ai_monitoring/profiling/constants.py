"""
Constants for the ai_monitoring.profiling module.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------

START: Final[str] = "start"
STOP: Final[str] = "stop"
GET: Final[str] = "get"
LIST: Final[str] = "list"
RESET: Final[str] = "reset"

SUPPORTED_OPERATIONS: Final[tuple[str, ...]] = (
    START,
    STOP,
    GET,
    LIST,
    RESET,
)

# ---------------------------------------------------------------------------
# Profile types
# ---------------------------------------------------------------------------

CPU: Final[str] = "cpu"
MEMORY: Final[str] = "memory"
NETWORK: Final[str] = "network"
IO: Final[str] = "io"

SUPPORTED_PROFILE_TYPES: Final[tuple[str, ...]] = (
    CPU,
    MEMORY,
    NETWORK,
    IO,
)

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_PROFILE_ID: Final[str] = "profile_id"
METADATA_PROFILE_TYPE: Final[str] = "profile_type"
METADATA_TIMESTAMP: Final[str] = "timestamp"
METADATA_DURATION: Final[str] = "duration_ms"
METADATA_STATUS: Final[str] = "status"