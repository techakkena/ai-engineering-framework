"""
Unit tests for ai_multimodal.embeddings.operations.
"""

from __future__ import annotations

import pytest

from ai_multimodal.embeddings.exceptions import (
    EmbeddingComparisonError,
    EmbeddingCreationError,
    EmbeddingMetadataError,
    EmbeddingSearchError,
    EmbeddingUpdateError,
    EmbeddingValidationError,
    UnsupportedEmbeddingTypeError,
    UnsupportedSimilarityMetricError,
)
from ai_multimodal.embeddings.operations import (
    EmbeddingResult,
    compare_embeddings,
    create_embedding,
    get_embedding_metadata,
    search_similar_embeddings,
    update_embedding,
)


def test_create_embedding_success() -> None:
    """Embedding creation should succeed."""
    result = create_embedding("Hello World")

    assert isinstance(result, EmbeddingResult)
    assert result.success is True
    assert result.task == "create"


def test_create_embedding_empty_content() -> None:
    """Empty content should raise."""
    with pytest.raises(EmbeddingValidationError):
        create_embedding("")


def test_create_embedding_invalid_type() -> None:
    """Unsupported embedding types should raise."""
    with pytest.raises(UnsupportedEmbeddingTypeError):
        create_embedding(
            "Hello",
            embedding_type="custom",
        )


def test_create_embedding_invalid_dimensions() -> None:
    """Invalid dimensions should raise."""
    with pytest.raises(EmbeddingCreationError):
        create_embedding(
            "Hello",
            dimensions=100000,
        )


def test_compare_embeddings_success() -> None:
    """Embedding comparison should succeed."""
    result = compare_embeddings(
        [0.1, 0.2],
        [0.1, 0.2],
    )

    assert result.success is True
    assert result.task == "compare"


def test_compare_embeddings_invalid_metric() -> None:
    """Unsupported similarity metric should raise."""
    with pytest.raises(UnsupportedSimilarityMetricError):
        compare_embeddings(
            [0.1],
            [0.1],
            similarity_metric="invalid",
        )


def test_compare_embeddings_dimension_mismatch() -> None:
    """Dimension mismatch should raise."""
    with pytest.raises(EmbeddingComparisonError):
        compare_embeddings(
            [0.1],
            [0.1, 0.2],
        )


def test_search_embeddings_success() -> None:
    """Embedding search should succeed."""
    result = search_similar_embeddings([0.1, 0.2])

    assert result.success is True
    assert result.task == "search"


def test_search_embeddings_invalid_top_k() -> None:
    """Invalid top_k should raise."""
    with pytest.raises(EmbeddingSearchError):
        search_similar_embeddings(
            [0.1],
            top_k=0,
        )


def test_update_embedding_success() -> None:
    """Embedding update should succeed."""
    result = update_embedding(
        "embedding-1",
        [0.1, 0.2],
    )

    assert result.success is True
    assert result.task == "update"


def test_update_embedding_invalid_identifier() -> None:
    """Empty embedding identifiers should raise."""
    with pytest.raises(EmbeddingUpdateError):
        update_embedding("", [0.1])


def test_get_embedding_metadata_success() -> None:
    """Metadata retrieval should succeed."""
    result = get_embedding_metadata("embedding-1")

    assert result.success is True
    assert result.task == "metadata"


def test_get_embedding_metadata_invalid_identifier() -> None:
    """Empty embedding identifiers should raise."""
    with pytest.raises(EmbeddingMetadataError):
        get_embedding_metadata("")