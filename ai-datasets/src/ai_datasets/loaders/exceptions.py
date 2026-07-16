"""
Exceptions for the ai_datasets.loaders package.

This module defines the exception hierarchy for provider-independent
dataset loading operations.
"""

from __future__ import annotations


class DatasetLoaderError(Exception):
    """Base exception for all dataset loader errors."""


class LoaderValidationError(DatasetLoaderError):
    """Raised when loader input validation fails."""


class UnsupportedLoaderError(LoaderValidationError):
    """Raised when an unsupported loader is requested."""


class DatasetLoadingError(DatasetLoaderError):
    """Base exception for dataset loading failures."""


class CSVLoaderError(DatasetLoadingError):
    """Raised when loading a CSV dataset fails."""


class JSONLoaderError(DatasetLoadingError):
    """Raised when loading a JSON dataset fails."""


class ParquetLoaderError(DatasetLoadingError):
    """Raised when loading a Parquet dataset fails."""


class TextLoaderError(DatasetLoadingError):
    """Raised when loading a text dataset fails."""


class DatabaseLoaderError(DatasetLoadingError):
    """Raised when loading data from a database fails."""


class DatasetSourceError(DatasetLoaderError):
    """Raised when a dataset source cannot be accessed."""