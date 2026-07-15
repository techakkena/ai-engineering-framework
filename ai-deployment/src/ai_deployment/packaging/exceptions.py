"""
Exceptions for the packaging module.
"""

from __future__ import annotations


class PackagingError(Exception):
    """Base exception for packaging operations."""


class PackagingConfigurationError(PackagingError):
    """Raised when packaging configuration is invalid."""


class PackageBuildError(PackagingError):
    """Raised when package creation fails."""