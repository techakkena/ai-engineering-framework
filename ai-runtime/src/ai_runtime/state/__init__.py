"""
ai_runtime.state

Framework-independent runtime state utilities.

This module provides reusable constants, exceptions, and helper
operations for managing runtime state.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_runtime.state.constants import (
    DEFAULT_STATE_NAME,
    DEFAULT_STATE_STATUS,
    DEFAULT_STATE_TYPE,
    SUPPORTED_STATE_STATUSES,
)
from ai_runtime.state.exceptions import (
    InvalidStateStatusError,
    StateConfigurationError,
    StateError,
    StateValidationError,
)
from ai_runtime.state.operations import (
    build_state_id,
    is_supported_state_status,
    normalize_state_status,
    validate_state_id,
    validate_state_status,
)

__all__ = [
    # Constants
    "DEFAULT_STATE_NAME",
    "DEFAULT_STATE_STATUS",
    "DEFAULT_STATE_TYPE",
    "SUPPORTED_STATE_STATUSES",
    # Exceptions
    "StateError",
    "InvalidStateStatusError",
    "StateConfigurationError",
    "StateValidationError",
    # Operations
    "build_state_id",
    "is_supported_state_status",
    "normalize_state_status",
    "validate_state_id",
    "validate_state_status",
]