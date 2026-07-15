"""
Exceptions for integration utilities.
"""

from __future__ import annotations


class IntegrationError(Exception):
    """Base exception for integration utilities."""


class RetryError(IntegrationError):
    """Raised when retry attempts are exhausted."""


class ValidationError(IntegrationError):
    """Raised when validation fails."""


class SerializationError(IntegrationError):
    """Raised when serialization fails."""