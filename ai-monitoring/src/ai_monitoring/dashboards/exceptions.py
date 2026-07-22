"""
Exceptions for the ai_monitoring.dashboards package.
"""

from __future__ import annotations


class DashboardError(Exception):
    """Base exception for dashboard errors."""


class DashboardValidationError(DashboardError):
    """Raised when dashboard validation fails."""


class DashboardNotFoundError(DashboardError):
    """Raised when a dashboard cannot be found."""


class DashboardCreationError(DashboardError):
    """Raised when dashboard creation fails."""


class DashboardUpdateError(DashboardError):
    """Raised when dashboard update fails."""


class DashboardConfigurationError(DashboardError):
    """Raised when dashboard configuration is invalid."""


class DashboardProviderError(DashboardError):
    """Raised when an underlying dashboard provider fails."""