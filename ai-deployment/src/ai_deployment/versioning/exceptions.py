"""
Exceptions for the versioning module.
"""

from __future__ import annotations


class VersionError(Exception):
    """Base exception for version operations."""


class VersionFormatError(VersionError):
    """Raised when a version string is invalid."""


class VersionValidationError(VersionError):
    """Raised when version validation fails."""