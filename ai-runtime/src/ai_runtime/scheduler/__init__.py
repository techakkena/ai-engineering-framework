"""
ai_runtime.scheduler

Framework-independent scheduling utilities.

This module provides reusable constants, exceptions, and helper
operations for scheduling runtime tasks.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_runtime.scheduler.constants import (
    DEFAULT_SCHEDULER_MODE,
    DEFAULT_SCHEDULER_NAME,
    DEFAULT_SCHEDULER_STATE,
    SUPPORTED_SCHEDULER_MODES,
)
from ai_runtime.scheduler.exceptions import (
    InvalidSchedulerModeError,
    SchedulerConfigurationError,
    SchedulerError,
    SchedulerValidationError,
)
from ai_runtime.scheduler.operations import (
    build_scheduler_id,
    is_supported_scheduler_mode,
    normalize_scheduler_mode,
    validate_scheduler_id,
    validate_scheduler_mode,
)

__all__ = [
    # Constants
    "DEFAULT_SCHEDULER_NAME",
    "DEFAULT_SCHEDULER_MODE",
    "DEFAULT_SCHEDULER_STATE",
    "SUPPORTED_SCHEDULER_MODES",
    # Exceptions
    "SchedulerError",
    "InvalidSchedulerModeError",
    "SchedulerConfigurationError",
    "SchedulerValidationError",
    # Operations
    "build_scheduler_id",
    "is_supported_scheduler_mode",
    "normalize_scheduler_mode",
    "validate_scheduler_id",
    "validate_scheduler_mode",
]