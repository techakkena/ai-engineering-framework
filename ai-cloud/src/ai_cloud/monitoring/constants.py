"""Constants for the ai_cloud.monitoring module."""

from __future__ import annotations

from typing import Final

DEFAULT_MONITOR_NAME: Final[str] = "monitor"
DEFAULT_MONITOR_TYPE: Final[str] = "metrics"
DEFAULT_ENABLED: Final[bool] = True

METRICS_MONITOR: Final[str] = "metrics"
LOGGING_MONITOR: Final[str] = "logging"
TRACING_MONITOR: Final[str] = "tracing"
HEALTH_MONITOR: Final[str] = "health"

SUPPORTED_MONITOR_TYPES: Final[frozenset[str]] = frozenset(
    {
        METRICS_MONITOR,
        LOGGING_MONITOR,
        TRACING_MONITOR,
        HEALTH_MONITOR,
    }
)

MIN_MONITOR_NAME_LENGTH: Final[int] = 1
MAX_MONITOR_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
INTERVAL_KEY: Final[str] = "interval"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_ENABLED",
    "DEFAULT_MONITOR_NAME",
    "DEFAULT_MONITOR_TYPE",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "HEALTH_MONITOR",
    "INTERVAL_KEY",
    "LOGGING_MONITOR",
    "MAX_MONITOR_NAME_LENGTH",
    "METRICS_MONITOR",
    "MIN_MONITOR_NAME_LENGTH",
    "NAME_KEY",
    "SUPPORTED_MONITOR_TYPES",
    "TRACING_MONITOR",
    "TYPE_KEY",
]