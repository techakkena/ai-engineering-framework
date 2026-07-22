"""
Exceptions for the ai_monitoring.collectors package.
"""

from __future__ import annotations


class CollectorError(Exception):
    """Base exception for collector errors."""


class CollectorValidationError(CollectorError):
    """Raised when collector validation fails."""


class CollectorNotFoundError(CollectorError):
    """Raised when a collector cannot be found."""


class CollectionError(CollectorError):
    """Raised when data collection fails."""


class CollectorConfigurationError(CollectorError):
    """Raised when collector configuration is invalid."""


class CollectorProviderError(CollectorError):
    """Raised when a collector provider fails."""