"""Constants for the ai_analytics.metrics module."""

from __future__ import annotations

from typing import Final

# Default metric configuration.
DEFAULT_METRIC_NAME: Final[str] = "metric"
DEFAULT_METRIC_TYPE: Final[str] = "counter"
DEFAULT_ENABLED: Final[bool] = True

# Supported metric types.
COUNTER_TYPE: Final[str] = "counter"
GAUGE_TYPE: Final[str] = "gauge"
HISTOGRAM_TYPE: Final[str] = "histogram"
SUMMARY_TYPE: Final[str] = "summary"

SUPPORTED_METRIC_TYPES: Final[frozenset[str]] = frozenset(
    {
        COUNTER_TYPE,
        GAUGE_TYPE,
        HISTOGRAM_TYPE,
        SUMMARY_TYPE,
    }
)

# Validation.
MIN_METRIC_NAME_LENGTH: Final[int] = 1
MAX_METRIC_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
VALUE_KEY: Final[str] = "value"
DESCRIPTION_KEY: Final[str] = "description"
TAGS_KEY: Final[str] = "tags"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "COUNTER_TYPE",
    "DEFAULT_ENABLED",
    "DEFAULT_METRIC_NAME",
    "DEFAULT_METRIC_TYPE",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "GAUGE_TYPE",
    "HISTOGRAM_TYPE",
    "MAX_METRIC_NAME_LENGTH",
    "MIN_METRIC_NAME_LENGTH",
    "NAME_KEY",
    "SUMMARY_TYPE",
    "SUPPORTED_METRIC_TYPES",
    "TAGS_KEY",
    "TYPE_KEY",
    "VALUE_KEY",
]