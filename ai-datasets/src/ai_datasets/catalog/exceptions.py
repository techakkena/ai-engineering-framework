"""
Exceptions for the ai_datasets.catalog package.
"""

from __future__ import annotations


class DatasetCatalogError(Exception):
    """Base exception for dataset catalog errors."""


class CatalogValidationError(DatasetCatalogError):
    """Raised when catalog validation fails."""


class DatasetAlreadyExistsError(DatasetCatalogError):
    """Raised when attempting to register an existing dataset."""


class DatasetNotFoundError(DatasetCatalogError):
    """Raised when a dataset cannot be found."""


class CatalogRegistrationError(DatasetCatalogError):
    """Raised when dataset registration fails."""


class CatalogSearchError(DatasetCatalogError):
    """Raised when dataset search fails."""


class CatalogConfigurationError(DatasetCatalogError):
    """Raised when the catalog configuration is invalid."""


class CatalogProviderError(DatasetCatalogError):
    """Raised when a catalog provider fails."""