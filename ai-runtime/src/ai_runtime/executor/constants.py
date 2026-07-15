"""
Constants for ai_runtime.executor.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Executor Defaults
# ============================================================================

DEFAULT_EXECUTOR_NAME: Final[str] = "executor"

DEFAULT_EXECUTOR_MODE: Final[str] = "sequential"

DEFAULT_EXECUTOR_STATE: Final[str] = "idle"

# ============================================================================
# Executor Modes
# ============================================================================

SEQUENTIAL_MODE: Final[str] = "sequential"

PARALLEL_MODE: Final[str] = "parallel"

ASYNC_MODE: Final[str] = "async"

SUPPORTED_EXECUTOR_MODES: Final[frozenset[str]] = frozenset(
    {
        SEQUENTIAL_MODE,
        PARALLEL_MODE,
        ASYNC_MODE,
    }
)

# ============================================================================
# Executor States
# ============================================================================

IDLE_STATE: Final[str] = "idle"

RUNNING_STATE: Final[str] = "running"

COMPLETED_STATE: Final[str] = "completed"

FAILED_STATE: Final[str] = "failed"

SUPPORTED_EXECUTOR_STATES: Final[frozenset[str]] = frozenset(
    {
        IDLE_STATE,
        RUNNING_STATE,
        COMPLETED_STATE,
        FAILED_STATE,
    }
)

# ============================================================================
# Executor Configuration
# ============================================================================

DEFAULT_MAX_CONCURRENCY: Final[int] = 10

DEFAULT_EXECUTION_TIMEOUT: Final[int] = 300