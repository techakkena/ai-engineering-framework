"""
Exceptions for the ai_datasets.registry package.
"""

from __future__ import annotations


class DatasetRegistryError(Exception):
    """Base exception for dataset registry errors."""


class RegistryValidationError(DatasetRegistryError):
    """Raised when registry validation fails."""


class DatasetAlreadyRegisteredError(DatasetRegistryError):
    """Raised when a dataset is already registered."""


class DatasetNotRegisteredError(DatasetRegistryError):
    """Raised when a dataset is not registered."""


class RegistryOperationError(DatasetRegistryError):
    """Raised when a registry operation fails."""


class RegistryConfigurationError(DatasetRegistryError):
    """Raised when the registry configuration is invalid."""


class RegistryProviderError(DatasetRegistryError):
    """Raised when an underlying registry provider fails."""