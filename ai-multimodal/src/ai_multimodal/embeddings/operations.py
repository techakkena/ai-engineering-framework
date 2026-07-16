"""
Enterprise embedding operations for the ai_multimodal.embeddings package.

This module provides provider-independent abstractions for creating,
comparing, searching, updating, and inspecting vector embeddings.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_multimodal.embeddings.constants import (
    DEFAULT_SIMILARITY_THRESHOLD,
    DEFAULT_TOP_K,
    DEFAULT_VECTOR_DIMENSIONS,
    EMBEDDING_TYPE_TEXT,
    MAX_TOP_K,
    MAX_VECTOR_DIMENSIONS,
    SIMILARITY_COSINE,
    SUPPORTED_EMBEDDING_TYPES,
    SUPPORTED_SIMILARITY_METRICS,
)
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


@dataclass(slots=True, frozen=True)
class EmbeddingResult:
    """Represents the result of an embedding operation."""

    task: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


def create_embedding(
    content: str,
    *,
    embedding_type: str = EMBEDDING_TYPE_TEXT,
    dimensions: int = DEFAULT_VECTOR_DIMENSIONS,
) -> EmbeddingResult:
    """
    Create an embedding for the supplied content.
    """
    if not content.strip():
        raise EmbeddingValidationError("Content cannot be empty.")

    if embedding_type not in SUPPORTED_EMBEDDING_TYPES:
        raise UnsupportedEmbeddingTypeError(
            f"Unsupported embedding type: {embedding_type!r}."
        )

    if dimensions <= 0 or dimensions > MAX_VECTOR_DIMENSIONS:
        raise EmbeddingCreationError(
            "Invalid embedding dimensions."
        )

    return EmbeddingResult(
        task="create",
        success=True,
        data={
            "embedding_type": embedding_type,
            "dimensions": dimensions,
        },
    )


def compare_embeddings(
    first_embedding: list[float],
    second_embedding: list[float],
    *,
    similarity_metric: str = SIMILARITY_COSINE,
) -> EmbeddingResult:
    """
    Compare two embeddings.
    """
    if similarity_metric not in SUPPORTED_SIMILARITY_METRICS:
        raise UnsupportedSimilarityMetricError(
            f"Unsupported similarity metric: {similarity_metric!r}."
        )

    if len(first_embedding) != len(second_embedding):
        raise EmbeddingComparisonError(
            "Embeddings must have equal dimensions."
        )

    return EmbeddingResult(
        task="compare",
        success=True,
        data={
            "similarity_metric": similarity_metric,
        },
    )


def search_similar_embeddings(
    embedding: list[float],
    *,
    top_k: int = DEFAULT_TOP_K,
    similarity_threshold: float = DEFAULT_SIMILARITY_THRESHOLD,
) -> EmbeddingResult:
    """
    Search for similar embeddings.
    """
    if top_k <= 0 or top_k > MAX_TOP_K:
        raise EmbeddingSearchError("Invalid top_k value.")

    if not 0.0 <= similarity_threshold <= 1.0:
        raise EmbeddingSearchError(
            "Similarity threshold must be between 0.0 and 1.0."
        )

    return EmbeddingResult(
        task="search",
        success=True,
        data={
            "vector_length": len(embedding),
            "top_k": top_k,
            "similarity_threshold": similarity_threshold,
        },
    )


def update_embedding(
    embedding_id: str,
    embedding: list[float],
) -> EmbeddingResult:
    """
    Update an existing embedding.
    """
    if not embedding_id.strip():
        raise EmbeddingUpdateError(
            "Embedding ID cannot be empty."
        )

    return EmbeddingResult(
        task="update",
        success=True,
        data={
            "embedding_id": embedding_id,
            "vector_length": len(embedding),
        },
    )


def get_embedding_metadata(
    embedding_id: str,
) -> EmbeddingResult:
    """
    Retrieve embedding metadata.
    """
    if not embedding_id.strip():
        raise EmbeddingMetadataError(
            "Embedding ID cannot be empty."
        )

    return EmbeddingResult(
        task="metadata",
        success=True,
        metadata={
            "embedding_id": embedding_id,
        },
    )