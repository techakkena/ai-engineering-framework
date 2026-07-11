"""
Custom exceptions for the logging package.

This module defines the exception hierarchy used by the logging
subsystem. Keeping logging-specific exceptions separate allows
callers to catch precise errors while maintaining a consistent
exception model across the AI Engineering Framework.
"""

from __future__ import annotations

__all__ = [
    "LoggingError",
    "LoggingConfigurationError",
    "LoggerCreationError",
]


class LoggingError(Exception):
    """Base exception for all logging-related errors."""


class LoggingConfigurationError(LoggingError):
    """Raised when the logging configuration is invalid."""


class LoggerCreationError(LoggingError):
    """Raised when a logger cannot be created or initialized."""
