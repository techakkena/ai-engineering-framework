"""
Exceptions for the ai_monitoring.logging package.
"""

from __future__ import annotations


class LoggingError(Exception):
    """Base exception for logging errors."""


class LogValidationError(LoggingError):
    """Raised when log validation fails."""


class LogNotFoundError(LoggingError):
    """Raised when a log entry cannot be found."""


class LogWriteError(LoggingError):
    """Raised when writing a log fails."""


class LogReadError(LoggingError):
    """Raised when reading logs fails."""


class LoggingConfigurationError(LoggingError):
    """Raised when logging configuration is invalid."""


class LoggingProviderError(LoggingError):
    """Raised when an underlying logging provider fails."""