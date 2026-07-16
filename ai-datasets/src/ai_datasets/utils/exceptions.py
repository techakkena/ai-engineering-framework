"""
Exceptions for the ai_datasets.utils package.
"""

from __future__ import annotations


class DatasetUtilsError(Exception):
    """Base exception for dataset utility errors."""


class UtilityValidationError(DatasetUtilsError):
    """Raised when utility validation fails."""


class DatasetInspectionError(DatasetUtilsError):
    """Raised when dataset inspection fails."""


class SchemaInferenceError(DatasetUtilsError):
    """Raised when schema inference fails."""


class DatasetStatisticsError(DatasetUtilsError):
    """Raised when statistics generation fails."""


class UtilityConfigurationError(DatasetUtilsError):
    """Raised when utility configuration is invalid."""


class UtilityProviderError(DatasetUtilsError):
    """Raised when an underlying utility provider fails."""