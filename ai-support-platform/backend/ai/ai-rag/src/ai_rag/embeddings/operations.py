from __future__ import annotations

"""Operations for embedding models."""

from .constants import (
    DEFAULT_EMBEDDING_DIMENSIONS,
    DEFAULT_EMBEDDING_MODEL,
    MODEL_DIMENSIONS,
    SUPPORTED_EMBEDDING_MODELS,
)


def default_embedding_model() -> str:
    """Return the default embedding model."""

    return DEFAULT_EMBEDDING_MODEL


def supported_embedding_model(model: str) -> bool:
    """Return True if the embedding model is supported."""

    return model in SUPPORTED_EMBEDDING_MODELS


def embedding_dimensions(model: str) -> int:
    """Return the dimensions for an embedding model."""

    return MODEL_DIMENSIONS.get(
        model,
        DEFAULT_EMBEDDING_DIMENSIONS,
    )


def valid_embedding_vector(vector: list[float]) -> bool:
    """Validate an embedding vector."""

    if not vector:
        return False

    return all(
        isinstance(value, float)
        for value in vector
    )
