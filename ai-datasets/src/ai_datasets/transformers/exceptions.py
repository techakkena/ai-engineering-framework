"""
Exceptions for the ai_datasets.transformers package.

This module defines the exception hierarchy for provider-independent
dataset transformation operations.
"""

from __future__ import annotations


class DatasetTransformerError(Exception):
    """Base exception for all dataset transformer errors."""


class TransformerValidationError(DatasetTransformerError):
    """Raised when transformer input validation fails."""


class UnsupportedTransformationError(TransformerValidationError):
    """Raised when an unsupported transformation is requested."""


class DatasetTransformationError(DatasetTransformerError):
    """Base exception for dataset transformation failures."""


class FilterTransformationError(DatasetTransformationError):
    """Raised when dataset filtering fails."""


class MapTransformationError(DatasetTransformationError):
    """Raised when dataset mapping fails."""


class NormalizationError(DatasetTransformationError):
    """Raised when dataset normalization fails."""


class BatchTransformationError(DatasetTransformationError):
    """Raised when dataset batching fails."""


class DatasetPipelineError(DatasetTransformationError):
    """Raised when a dataset transformation pipeline fails."""


class DatasetTransformerProviderError(DatasetTransformerError):
    """Raised when an underlying transformer provider returns an error."""