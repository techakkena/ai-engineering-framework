"""Constants for the ai_optimization.scheduling module."""

from __future__ import annotations

from typing import Final

# Default scheduling configuration.
DEFAULT_SCHEDULE_NAME: Final[str] = "schedule"
DEFAULT_SCHEDULER: Final[str] = "fifo"
DEFAULT_ENABLED: Final[bool] = True

# Supported schedulers.
FIFO_SCHEDULER: Final[str] = "fifo"
PRIORITY_SCHEDULER: Final[str] = "priority"
ROUND_ROBIN_SCHEDULER: Final[str] = "round_robin"
ADAPTIVE_SCHEDULER: Final[str] = "adaptive"

SUPPORTED_SCHEDULERS: Final[frozenset[str]] = frozenset(
    {
        FIFO_SCHEDULER,
        PRIORITY_SCHEDULER,
        ROUND_ROBIN_SCHEDULER,
        ADAPTIVE_SCHEDULER,
    }
)

# Validation.
MIN_SCHEDULE_NAME_LENGTH: Final[int] = 1
MAX_SCHEDULE_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
SCHEDULER_KEY: Final[str] = "scheduler"
MAX_CONCURRENCY_KEY: Final[str] = "max_concurrency"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "ADAPTIVE_SCHEDULER",
    "DEFAULT_ENABLED",
    "DEFAULT_SCHEDULE_NAME",
    "DEFAULT_SCHEDULER",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "FIFO_SCHEDULER",
    "MAX_CONCURRENCY_KEY",
    "MAX_SCHEDULE_NAME_LENGTH",
    "MIN_SCHEDULE_NAME_LENGTH",
    "NAME_KEY",
    "PRIORITY_SCHEDULER",
    "ROUND_ROBIN_SCHEDULER",
    "SCHEDULER_KEY",
    "SUPPORTED_SCHEDULERS",
]