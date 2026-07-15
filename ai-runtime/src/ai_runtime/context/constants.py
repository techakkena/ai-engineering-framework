"""
Constants for ai_runtime.context.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Context Defaults
# ============================================================================

DEFAULT_CONTEXT_ID: Final[str] = "context"

DEFAULT_CONTEXT_SCOPE: Final[str] = "request"

DEFAULT_CONTEXT_STATE: Final[str] = "active"

# ============================================================================
# Context Scopes
# ============================================================================

REQUEST_SCOPE: Final[str] = "request"

SESSION_SCOPE: Final[str] = "session"

WORKFLOW_SCOPE: Final[str] = "workflow"

AGENT_SCOPE: Final[str] = "agent"

GLOBAL_SCOPE: Final[str] = "global"

SUPPORTED_CONTEXT_SCOPES: Final[frozenset[str]] = frozenset(
    {
        REQUEST_SCOPE,
        SESSION_SCOPE,
        WORKFLOW_SCOPE,
        AGENT_SCOPE,
        GLOBAL_SCOPE,
    }
)

# ============================================================================
# Context States
# ============================================================================

ACTIVE_STATE: Final[str] = "active"

INACTIVE_STATE: Final[str] = "inactive"

EXPIRED_STATE: Final[str] = "expired"

SUPPORTED_CONTEXT_STATES: Final[frozenset[str]] = frozenset(
    {
        ACTIVE_STATE,
        INACTIVE_STATE,
        EXPIRED_STATE,
    }
)

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_CONTEXT_TIMEOUT: Final[int] = 300

DEFAULT_MAX_CONTEXT_SIZE: Final[int] = 1024