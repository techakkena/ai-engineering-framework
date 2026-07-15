"""
ai_runtime.lifecycle

Framework-independent lifecycle management utilities.

This module provides reusable constants, exceptions, and helper
operations for managing the lifecycle of runtime components.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_runtime.lifecycle.constants import (
    DEFAULT_LIFECYCLE_NAME,
    DEFAULT_LIFECYCLE_PHASE,
    DEFAULT_LIFECYCLE_STATE,
    SUPPORTED_LIFECYCLE_PHASES,
)
from ai_runtime.lifecycle.exceptions import (
    InvalidLifecyclePhaseError,
    LifecycleConfigurationError,
    LifecycleError,
    LifecycleValidationError,
)
from ai_runtime.lifecycle.operations import (
    build_lifecycle_id,
    is_supported_lifecycle_phase,
    normalize_lifecycle_phase,
    validate_lifecycle_id,
    validate_lifecycle_phase,
)

__all__ = [
    # Constants
    "DEFAULT_LIFECYCLE_NAME",
    "DEFAULT_LIFECYCLE_PHASE",
    "DEFAULT_LIFECYCLE_STATE",
    "SUPPORTED_LIFECYCLE_PHASES",
    # Exceptions
    "LifecycleError",
    "InvalidLifecyclePhaseError",
    "LifecycleConfigurationError",
    "LifecycleValidationError",
    # Operations
    "build_lifecycle_id",
    "is_supported_lifecycle_phase",
    "normalize_lifecycle_phase",
    "validate_lifecycle_id",
    "validate_lifecycle_phase",
]