"""
Exceptions for the ai_monitoring.metrics package.
"""

from __future__ import annotations


class MetricsError(Exception):
    """Base exception for metrics errors."""


class MetricValidationError(MetricsError):
    """Raised when metric validation fails."""


class MetricNotFoundError(MetricsError):
    """Raised when a metric cannot be found."""


class MetricCollectionError(MetricsError):
    """Raised when metric collection fails."""


class MetricRecordingError(MetricsError):
    """Raised when metric recording fails."""


class MetricsConfigurationError(MetricsError):
    """Raised when metrics configuration is invalid."""


class MetricsProviderError(MetricsError):
    """Raised when an underlying metrics provider fails."""