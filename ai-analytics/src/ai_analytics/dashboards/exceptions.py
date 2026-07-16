"""Exceptions for the ai_analytics.dashboards module."""

from __future__ import annotations


class DashboardError(Exception):
    """Base exception for dashboard operations."""


class DashboardValidationError(DashboardError):
    """Raised when dashboard validation fails."""


class DashboardRegistrationError(DashboardError):
    """Raised when dashboard registration fails."""


class DashboardNotFoundError(
    DashboardRegistrationError,
):
    """Raised when a dashboard cannot be found."""


class DuplicateDashboardError(
    DashboardRegistrationError,
):
    """Raised when attempting to register a duplicate dashboard."""


class UnsupportedLayoutError(
    DashboardValidationError,
):
    """Raised when an unsupported dashboard layout is supplied."""


__all__ = [
    "DashboardError",
    "DashboardNotFoundError",
    "DashboardRegistrationError",
    "DashboardValidationError",
    "DuplicateDashboardError",
    "UnsupportedLayoutError",
]