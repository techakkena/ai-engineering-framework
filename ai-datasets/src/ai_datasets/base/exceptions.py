"""
Exceptions for the ai_datasets.base package.

This module defines the exception hierarchy for provider-independent
dataset operations.
"""

from __future__ import annotations


class DatasetError(Exception):
    """Base exception for all dataset-related errors."""


class DatasetValidationError(DatasetError):
    """Raised when dataset validation fails."""


class UnsupportedDatasetTypeError(DatasetValidationError):
    """Raised when an unsupported dataset type is requested."""


class InvalidDatasetError(DatasetValidationError):
    """Raised when a dataset is invalid or malformed."""


class DatasetProcessingError(DatasetError):
    """Base exception for dataset processing failures."""


class DatasetCreationError(DatasetProcessingError):
    """Raised when dataset creation fails."""


class DatasetLoadingError(DatasetProcessingError):
    """Raised when dataset loading fails."""


class DatasetSavingError(DatasetProcessingError):
    """Raised when dataset saving fails."""


class DatasetMetadataError(DatasetProcessingError):
    """Raised when dataset metadata operations fail."""


class DatasetProviderError(DatasetError):
    """Raised when an underlying dataset provider returns an error."""