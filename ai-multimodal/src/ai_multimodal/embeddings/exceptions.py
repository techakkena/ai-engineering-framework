"""
Exceptions for the ai_multimodal.embeddings package.

This module defines the exception hierarchy for provider-independent
embedding operations.
"""

from __future__ import annotations


class EmbeddingError(Exception):
    """Base exception for all embedding-related errors."""


class EmbeddingValidationError(EmbeddingError):
    """Raised when embedding input validation fails."""


class UnsupportedEmbeddingTypeError(EmbeddingValidationError):
    """Raised when an unsupported embedding type is requested."""


class UnsupportedSimilarityMetricError(EmbeddingValidationError):
    """Raised when an unsupported similarity metric is requested."""


class EmbeddingProcessingError(EmbeddingError):
    """Base exception for embedding processing failures."""


class EmbeddingCreationError(EmbeddingProcessingError):
    """Raised when embedding creation fails."""


class EmbeddingComparisonError(EmbeddingProcessingError):
    """Raised when embedding comparison fails."""


class EmbeddingSearchError(EmbeddingProcessingError):
    """Raised when embedding search fails."""


class EmbeddingUpdateError(EmbeddingProcessingError):
    """Raised when embedding update fails."""


class EmbeddingMetadataError(EmbeddingProcessingError):
    """Raised when embedding metadata retrieval fails."""


class EmbeddingProviderError(EmbeddingError):
    """Raised when an underlying embedding provider returns an error."""