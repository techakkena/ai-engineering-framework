"""
Constants for the ai_runtime.base module.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Runtime Defaults
# ============================================================================

DEFAULT_RUNTIME_NAME: Final[str] = "AI Runtime"

DEFAULT_RUNTIME_VERSION: Final[str] = "1.0.0"

DEFAULT_RUNTIME_STATUS: Final[str] = "initialized"

# ============================================================================
# Runtime Status
# ============================================================================

INITIALIZED: Final[str] = "initialized"

STARTING: Final[str] = "starting"

RUNNING: Final[str] = "running"

PAUSED: Final[str] = "paused"

STOPPING: Final[str] = "stopping"

STOPPED: Final[str] = "stopped"

FAILED: Final[str] = "failed"

SUPPORTED_RUNTIME_STATUSES: Final[frozenset[str]] = frozenset(
    {
        INITIALIZED,
        STARTING,
        RUNNING,
        PAUSED,
        STOPPING,
        STOPPED,
        FAILED,
    }
)

# ============================================================================
# Runtime Metadata
# ============================================================================

DEFAULT_ENCODING: Final[str] = "utf-8"

DEFAULT_TIMEOUT: Final[int] = 30

DEFAULT_MAX_WORKERS: Final[int] = 4