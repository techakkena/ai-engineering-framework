"""
Exceptions for the ai_datasets.versioning package.
"""

from __future__ import annotations


class DatasetVersioningError(Exception):
    """Base exception for dataset versioning errors."""


class VersionValidationError(DatasetVersioningError):
    """Raised when version validation fails."""


class VersionAlreadyExistsError(DatasetVersioningError):
    """Raised when a version already exists."""


class VersionNotFoundError(DatasetVersioningError):
    """Raised when a version cannot be found."""


class VersionComparisonError(DatasetVersioningError):
    """Raised when version comparison fails."""


class VersionRollbackError(DatasetVersioningError):
    """Raised when rollback fails."""


class VersionConfigurationError(DatasetVersioningError):
    """Raised when versioning configuration is invalid."""


class VersionProviderError(DatasetVersioningError):
    """Raised when an underlying version provider fails."""