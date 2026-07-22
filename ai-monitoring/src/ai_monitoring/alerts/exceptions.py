"""
Exceptions for the ai_monitoring.alerts package.
"""

from __future__ import annotations


class AlertError(Exception):
    """Base exception for alert errors."""


class AlertValidationError(AlertError):
    """Raised when alert validation fails."""


class AlertNotFoundError(AlertError):
    """Raised when an alert cannot be found."""


class AlertCreationError(AlertError):
    """Raised when alert creation fails."""


class AlertResolutionError(AlertError):
    """Raised when resolving an alert fails."""


class AlertConfigurationError(AlertError):
    """Raised when alert configuration is invalid."""


class AlertProviderError(AlertError):
    """Raised when an underlying alert provider fails."""