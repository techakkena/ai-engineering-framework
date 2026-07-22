"""
Exceptions for the ai_monitoring.health package.
"""

from __future__ import annotations


class HealthError(Exception):
    """Base exception for health monitoring errors."""


class HealthValidationError(HealthError):
    """Raised when health validation fails."""


class HealthCheckNotFoundError(HealthError):
    """Raised when a health check cannot be found."""


class HealthCheckError(HealthError):
    """Raised when a health check fails."""


class HealthConfigurationError(HealthError):
    """Raised when health monitoring configuration is invalid."""


class HealthProviderError(HealthError):
    """Raised when an underlying health provider fails."""