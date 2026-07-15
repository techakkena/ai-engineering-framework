"""
Constants for ai_runtime.lifecycle.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Lifecycle Defaults
# ============================================================================

DEFAULT_LIFECYCLE_NAME: Final[str] = "lifecycle"

DEFAULT_LIFECYCLE_PHASE: Final[str] = "created"

DEFAULT_LIFECYCLE_STATE: Final[str] = "inactive"

# ============================================================================
# Lifecycle Phases
# ============================================================================

CREATED_PHASE: Final[str] = "created"

INITIALIZING_PHASE: Final[str] = "initializing"

STARTING_PHASE: Final[str] = "starting"

RUNNING_PHASE: Final[str] = "running"

STOPPING_PHASE: Final[str] = "stopping"

STOPPED_PHASE: Final[str] = "stopped"

TERMINATED_PHASE: Final[str] = "terminated"

SUPPORTED_LIFECYCLE_PHASES: Final[frozenset[str]] = frozenset(
    {
        CREATED_PHASE,
        INITIALIZING_PHASE,
        STARTING_PHASE,
        RUNNING_PHASE,
        STOPPING_PHASE,
        STOPPED_PHASE,
        TERMINATED_PHASE,
    }
)

# ============================================================================
# Lifecycle States
# ============================================================================

ACTIVE_STATE: Final[str] = "active"

INACTIVE_STATE: Final[str] = "inactive"

FAILED_STATE: Final[str] = "failed"

SUPPORTED_LIFECYCLE_STATES: Final[frozenset[str]] = frozenset(
    {
        ACTIVE_STATE,
        INACTIVE_STATE,
        FAILED_STATE,
    }
)

# ============================================================================
# Lifecycle Configuration
# ============================================================================

DEFAULT_STARTUP_TIMEOUT: Final[int] = 60

DEFAULT_SHUTDOWN_TIMEOUT: Final[int] = 60