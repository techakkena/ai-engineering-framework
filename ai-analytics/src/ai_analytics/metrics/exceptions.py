"""Exceptions for the ai_analytics.metrics module."""

from __future__ import annotations


class MetricError(Exception):
    """Base exception for metric operations."""


class MetricValidationError(MetricError):
    """Raised when metric validation fails."""


class MetricRegistrationError(MetricError):
    """Raised when metric registration fails."""


class MetricNotFoundError(MetricRegistrationError):
    """Raised when a requested metric cannot be found."""


class DuplicateMetricError(MetricRegistrationError):
    """Raised when attempting to register a duplicate metric."""


class UnsupportedMetricTypeError(MetricValidationError):
    """Raised when an unsupported metric type is specified."""


__all__ = [
    "DuplicateMetricError",
    "MetricError",
    "MetricNotFoundError",
    "MetricRegistrationError",
    "MetricValidationError",
    "UnsupportedMetricTypeError",
]