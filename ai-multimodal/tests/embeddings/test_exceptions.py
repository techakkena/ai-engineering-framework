"""
Unit tests for ai_multimodal.embeddings.exceptions.
"""

from __future__ import annotations

import pytest

from ai_multimodal.embeddings.exceptions import (
    EmbeddingComparisonError,
    EmbeddingCreationError,
    EmbeddingError,
    EmbeddingMetadataError,
    EmbeddingProcessingError,
    EmbeddingProviderError,
    EmbeddingSearchError,
    EmbeddingUpdateError,
    EmbeddingValidationError,
    UnsupportedEmbeddingTypeError,
    UnsupportedSimilarityMetricError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        EmbeddingValidationError,
        UnsupportedEmbeddingTypeError,
        UnsupportedSimilarityMetricError,
        EmbeddingProcessingError,
        EmbeddingCreationError,
        EmbeddingComparisonError,
        EmbeddingSearchError,
        EmbeddingUpdateError,
        EmbeddingMetadataError,
        EmbeddingProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[EmbeddingError],
) -> None:
    """Every custom exception should inherit from EmbeddingError."""
    assert issubclass(exception_class, EmbeddingError)


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(EmbeddingError, match="embedding failure"):
        raise EmbeddingError("embedding failure")