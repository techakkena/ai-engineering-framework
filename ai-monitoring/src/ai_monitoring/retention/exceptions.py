"""
Exceptions for the ai_monitoring.retention package.
"""

from __future__ import annotations


class RetentionError(Exception):
    """Base exception for retention errors."""


class RetentionValidationError(RetentionError):
    """Raised when retention validation fails."""


class RetentionPolicyNotFoundError(RetentionError):
    """Raised when a retention policy cannot be found."""


class RetentionPolicyError(RetentionError):
    """Raised when retention policy execution fails."""


class RetentionConfigurationError(RetentionError):
    """Raised when retention configuration is invalid."""


class RetentionProviderError(RetentionError):
    """Raised when an underlying retention provider fails."""