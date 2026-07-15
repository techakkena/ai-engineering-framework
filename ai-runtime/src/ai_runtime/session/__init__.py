"""
ai_runtime.session

Framework-independent runtime session utilities.

This module provides reusable constants, exceptions, and helper
operations for managing runtime sessions.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_runtime.session.constants import (
    DEFAULT_SESSION_ID,
    DEFAULT_SESSION_STATE,
    DEFAULT_SESSION_TIMEOUT,
    SUPPORTED_SESSION_STATES,
)
from ai_runtime.session.exceptions import (
    InvalidSessionStateError,
    SessionConfigurationError,
    SessionError,
    SessionValidationError,
)
from ai_runtime.session.operations import (
    build_session_id,
    is_supported_session_state,
    normalize_session_state,
    validate_session_id,
    validate_session_state,
)

__all__ = [
    # Constants
    "DEFAULT_SESSION_ID",
    "DEFAULT_SESSION_STATE",
    "DEFAULT_SESSION_TIMEOUT",
    "SUPPORTED_SESSION_STATES",
    # Exceptions
    "SessionError",
    "InvalidSessionStateError",
    "SessionConfigurationError",
    "SessionValidationError",
    # Operations
    "build_session_id",
    "is_supported_session_state",
    "normalize_session_state",
    "validate_session_id",
    "validate_session_state",
]