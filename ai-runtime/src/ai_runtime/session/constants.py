"""
Constants for ai_runtime.session.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Session Defaults
# ============================================================================

DEFAULT_SESSION_ID: Final[str] = "session"

DEFAULT_SESSION_STATE: Final[str] = "created"

DEFAULT_SESSION_TIMEOUT: Final[int] = 1800

# ============================================================================
# Session States
# ============================================================================

CREATED_STATE: Final[str] = "created"

ACTIVE_STATE: Final[str] = "active"

IDLE_STATE: Final[str] = "idle"

EXPIRED_STATE: Final[str] = "expired"

CLOSED_STATE: Final[str] = "closed"

SUPPORTED_SESSION_STATES: Final[frozenset[str]] = frozenset(
    {
        CREATED_STATE,
        ACTIVE_STATE,
        IDLE_STATE,
        EXPIRED_STATE,
        CLOSED_STATE,
    }
)

# ============================================================================
# Session Configuration
# ============================================================================

DEFAULT_MAX_SESSIONS: Final[int] = 1000

DEFAULT_CLEANUP_INTERVAL: Final[int] = 300