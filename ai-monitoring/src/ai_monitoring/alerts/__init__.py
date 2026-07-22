"""
ai_monitoring.alerts

Enterprise alerts module for the AI Engineering Framework.

This package provides provider-independent alerting capabilities
for AI applications, infrastructure, and monitoring systems.

Modules
-------
constants
    Alert constants.

exceptions
    Alert exception hierarchy.

operations
    High-level alert operations.
"""

from ai_monitoring.alerts.operations import (
    acknowledge_alert,
    create_alert,
    get_alert,
    list_alerts,
    resolve_alert,
)

__all__ = [
    "create_alert",
    "acknowledge_alert",
    "resolve_alert",
    "get_alert",
    "list_alerts",
]