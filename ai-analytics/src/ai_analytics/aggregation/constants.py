"""Constants for the ai_analytics.aggregation module."""

from __future__ import annotations

from typing import Final

DEFAULT_AGGREGATION_NAME: Final[str] = "aggregation"
DEFAULT_AGGREGATION_TYPE: Final[str] = "sum"
DEFAULT_ENABLED: Final[bool] = True

SUM_AGGREGATION: Final[str] = "sum"
AVERAGE_AGGREGATION: Final[str] = "average"
MIN_AGGREGATION: Final[str] = "min"
MAX_AGGREGATION: Final[str] = "max"
COUNT_AGGREGATION: Final[str] = "count"

SUPPORTED_AGGREGATION_TYPES: Final[frozenset[str]] = frozenset(
    {
        SUM_AGGREGATION,
        AVERAGE_AGGREGATION,
        MIN_AGGREGATION,
        MAX_AGGREGATION,
        COUNT_AGGREGATION,
    }
)

MIN_AGGREGATION_NAME_LENGTH: Final[int] = 1
MAX_AGGREGATION_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
FIELD_KEY: Final[str] = "field"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "AVERAGE_AGGREGATION",
    "COUNT_AGGREGATION",
    "DEFAULT_AGGREGATION_NAME",
    "DEFAULT_AGGREGATION_TYPE",
    "DEFAULT_ENABLED",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "FIELD_KEY",
    "MAX_AGGREGATION",
    "MAX_AGGREGATION_NAME_LENGTH",
    "MIN_AGGREGATION",
    "MIN_AGGREGATION_NAME_LENGTH",
    "NAME_KEY",
    "SUM_AGGREGATION",
    "SUPPORTED_AGGREGATION_TYPES",
    "TYPE_KEY",
]