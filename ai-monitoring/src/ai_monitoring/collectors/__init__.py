"""
ai_monitoring.collectors

Enterprise collectors module for the AI Engineering Framework.

This package provides provider-independent monitoring data collectors
for metrics, logs, traces, telemetry, and health information.

Modules
-------
constants
    Collector constants.

exceptions
    Collector exception hierarchy.

operations
    High-level collector operations.
"""

from ai_monitoring.collectors.operations import (
    collect_data,
    get_collector,
    list_collectors,
    register_collector,
    remove_collector,
)

__all__ = [
    "register_collector",
    "collect_data",
    "get_collector",
    "list_collectors",
    "remove_collector",
]