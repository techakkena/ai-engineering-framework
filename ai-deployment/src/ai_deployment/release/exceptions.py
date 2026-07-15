"""
Exceptions for the release module.
"""

from __future__ import annotations


class ReleaseError(Exception):
    """Base exception for release operations."""


class ReleaseConfigurationError(ReleaseError):
    """Raised when release configuration is invalid."""


class ReleaseValidationError(ReleaseError):
    """Raised when release validation fails."""