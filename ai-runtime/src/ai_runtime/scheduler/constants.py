"""
Constants for ai_runtime.scheduler.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Scheduler Defaults
# ============================================================================

DEFAULT_SCHEDULER_NAME: Final[str] = "scheduler"

DEFAULT_SCHEDULER_MODE: Final[str] = "fifo"

DEFAULT_SCHEDULER_STATE: Final[str] = "idle"

# ============================================================================
# Scheduler Modes
# ============================================================================

FIFO_MODE: Final[str] = "fifo"

PRIORITY_MODE: Final[str] = "priority"

ROUND_ROBIN_MODE: Final[str] = "round_robin"

SUPPORTED_SCHEDULER_MODES: Final[frozenset[str]] = frozenset(
    {
        FIFO_MODE,
        PRIORITY_MODE,
        ROUND_ROBIN_MODE,
    }
)

# ============================================================================
# Scheduler States
# ============================================================================

IDLE_STATE: Final[str] = "idle"

RUNNING_STATE: Final[str] = "running"

PAUSED_STATE: Final[str] = "paused"

STOPPED_STATE: Final[str] = "stopped"

SUPPORTED_SCHEDULER_STATES: Final[frozenset[str]] = frozenset(
    {
        IDLE_STATE,
        RUNNING_STATE,
        PAUSED_STATE,
        STOPPED_STATE,
    }
)

# ============================================================================
# Scheduler Configuration
# ============================================================================

DEFAULT_MAX_QUEUE_SIZE: Final[int] = 1000

DEFAULT_POLL_INTERVAL: Final[int] = 5