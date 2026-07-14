"""Metric constants."""

from enum import Enum


class MetricType(str, Enum):
    """Supported metric types."""

    COUNTER = "counter"
    GAUGE = "gauge"
