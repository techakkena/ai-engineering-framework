"""
Constants for ai_runtime.state.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# State Defaults
# ============================================================================

DEFAULT_STATE_NAME: Final[str] = "state"

DEFAULT_STATE_STATUS: Final[str] = "pending"

DEFAULT_STATE_TYPE: Final[str] = "runtime"

# ============================================================================
# State Statuses
# ============================================================================

PENDING_STATUS: Final[str] = "pending"

READY_STATUS: Final[str] = "ready"

RUNNING_STATUS: Final[str] = "running"

COMPLETED_STATUS: Final[str] = "completed"

FAILED_STATUS: Final[str] = "failed"

CANCELLED_STATUS: Final[str] = "cancelled"

SUPPORTED_STATE_STATUSES: Final[frozenset[str]] = frozenset(
    {
        PENDING_STATUS,
        READY_STATUS,
        RUNNING_STATUS,
        COMPLETED_STATUS,
        FAILED_STATUS,
        CANCELLED_STATUS,
    }
)

# ============================================================================
# State Types
# ============================================================================

RUNTIME_STATE: Final[str] = "runtime"

WORKFLOW_STATE: Final[str] = "workflow"

TASK_STATE: Final[str] = "task"

AGENT_STATE: Final[str] = "agent"

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_STATE_HISTORY_SIZE: Final[int] = 100

DEFAULT_STATE_TIMEOUT: Final[int] = 300