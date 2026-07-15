"""
Constants for ai_runtime.runtime.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Runtime Defaults
# ============================================================================

DEFAULT_RUNTIME_ID: Final[str] = "runtime"

DEFAULT_RUNTIME_MODE: Final[str] = "sync"

DEFAULT_RUNTIME_STATE: Final[str] = "idle"

# ============================================================================
# Runtime Modes
# ============================================================================

SYNC_MODE: Final[str] = "sync"

ASYNC_MODE: Final[str] = "async"

DISTRIBUTED_MODE: Final[str] = "distributed"

SUPPORTED_RUNTIME_MODES: Final[frozenset[str]] = frozenset(
    {
        SYNC_MODE,
        ASYNC_MODE,
        DISTRIBUTED_MODE,
    }
)

# ============================================================================
# Runtime States
# ============================================================================

IDLE_STATE: Final[str] = "idle"

EXECUTING_STATE: Final[str] = "executing"

WAITING_STATE: Final[str] = "waiting"

COMPLETED_STATE: Final[str] = "completed"

FAILED_STATE: Final[str] = "failed"

SUPPORTED_RUNTIME_STATES: Final[frozenset[str]] = frozenset(
    {
        IDLE_STATE,
        EXECUTING_STATE,
        WAITING_STATE,
        COMPLETED_STATE,
        FAILED_STATE,
    }
)

# ============================================================================
# Runtime Configuration
# ============================================================================

DEFAULT_HEARTBEAT_INTERVAL: Final[int] = 30

DEFAULT_SHUTDOWN_TIMEOUT: Final[int] = 60