"""
ai_monitoring.dashboards

Enterprise dashboards module for the AI Engineering Framework.

This package provides provider-independent dashboard management,
creation, publishing, and querying capabilities for monitoring data.

Modules
-------
constants
    Dashboard constants.

exceptions
    Dashboard exception hierarchy.

operations
    High-level dashboard operations.
"""

from ai_monitoring.dashboards.operations import (
    create_dashboard,
    delete_dashboard,
    get_dashboard,
    list_dashboards,
    update_dashboard,
)

__all__ = [
    "create_dashboard",
    "get_dashboard",
    "update_dashboard",
    "delete_dashboard",
    "list_dashboards",
]