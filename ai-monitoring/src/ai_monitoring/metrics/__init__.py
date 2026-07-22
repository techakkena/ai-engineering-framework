"""
ai_monitoring.metrics

Enterprise metrics module for the AI Engineering Framework.

This package provides provider-independent metrics collection,
aggregation, reporting, and querying for AI applications.

Modules
-------
constants
    Metrics constants.

exceptions
    Metrics exception hierarchy.

operations
    High-level metrics operations.
"""

from ai_monitoring.metrics.operations import (
    collect_metric,
    get_metric,
    list_metrics,
    record_metric,
    reset_metrics,
)

__all__ = [
    "collect_metric",
    "record_metric",
    "get_metric",
    "list_metrics",
    "reset_metrics",
]