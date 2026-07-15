"""
ai_runtime.base

Framework-independent base runtime utilities.

This module provides reusable constants, exceptions, and helper
operations for the runtime layer.

The module serves as the foundation for runtime execution,
lifecycle management, and state handling.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_runtime.base.constants import (
    DEFAULT_RUNTIME_NAME,
    DEFAULT_RUNTIME_VERSION,
    DEFAULT_RUNTIME_STATUS,
    SUPPORTED_RUNTIME_STATUSES,
)
from ai_runtime.base.exceptions import (
    InvalidRuntimeError,
    RuntimeConfigurationError,
    RuntimeError,
    RuntimeValidationError,
)
from ai_runtime.base.operations import (
    build_runtime_name,
    is_supported_runtime_status,
    normalize_runtime_name,
    validate_runtime_name,
    validate_runtime_status,
)

__all__ = [
    # Constants
    "DEFAULT_RUNTIME_NAME",
    "DEFAULT_RUNTIME_VERSION",
    "DEFAULT_RUNTIME_STATUS",
    "SUPPORTED_RUNTIME_STATUSES",
    # Exceptions
    "RuntimeError",
    "InvalidRuntimeError",
    "RuntimeConfigurationError",
    "RuntimeValidationError",
    # Operations
    "build_runtime_name",
    "is_supported_runtime_status",
    "normalize_runtime_name",
    "validate_runtime_name",
    "validate_runtime_status",
]