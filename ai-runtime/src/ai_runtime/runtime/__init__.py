"""
ai_runtime.runtime

Framework-independent runtime execution utilities.

This module provides reusable constants, exceptions, and helper
operations for managing runtime execution.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_runtime.runtime.constants import (
    DEFAULT_RUNTIME_ID,
    DEFAULT_RUNTIME_MODE,
    DEFAULT_RUNTIME_STATE,
    SUPPORTED_RUNTIME_MODES,
)
from ai_runtime.runtime.exceptions import (
    InvalidRuntimeModeError,
    RuntimeExecutionError,
    RuntimeInitializationError,
    RuntimeStateError,
)
from ai_runtime.runtime.operations import (
    build_runtime_id,
    is_supported_runtime_mode,
    normalize_runtime_mode,
    validate_runtime_mode,
    validate_runtime_state,
)

__all__ = [
    # Constants
    "DEFAULT_RUNTIME_ID",
    "DEFAULT_RUNTIME_MODE",
    "DEFAULT_RUNTIME_STATE",
    "SUPPORTED_RUNTIME_MODES",
    # Exceptions
    "RuntimeExecutionError",
    "RuntimeInitializationError",
    "RuntimeStateError",
    "InvalidRuntimeModeError",
    # Operations
    "build_runtime_id",
    "is_supported_runtime_mode",
    "normalize_runtime_mode",
    "validate_runtime_mode",
    "validate_runtime_state",
]