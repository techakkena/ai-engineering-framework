"""
ai_runtime.executor

Framework-independent execution utilities.

This module provides reusable constants, exceptions, and helper
operations for executing runtime tasks.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_runtime.executor.constants import (
    DEFAULT_EXECUTOR_NAME,
    DEFAULT_EXECUTOR_MODE,
    DEFAULT_EXECUTOR_STATE,
    SUPPORTED_EXECUTOR_MODES,
)
from ai_runtime.executor.exceptions import (
    ExecutorConfigurationError,
    ExecutorError,
    ExecutorValidationError,
    InvalidExecutorModeError,
)
from ai_runtime.executor.operations import (
    build_executor_id,
    is_supported_executor_mode,
    normalize_executor_mode,
    validate_executor_id,
    validate_executor_mode,
)

__all__ = [
    # Constants
    "DEFAULT_EXECUTOR_NAME",
    "DEFAULT_EXECUTOR_MODE",
    "DEFAULT_EXECUTOR_STATE",
    "SUPPORTED_EXECUTOR_MODES",
    # Exceptions
    "ExecutorError",
    "InvalidExecutorModeError",
    "ExecutorConfigurationError",
    "ExecutorValidationError",
    # Operations
    "build_executor_id",
    "is_supported_executor_mode",
    "normalize_executor_mode",
    "validate_executor_id",
    "validate_executor_mode",
]