"""Embedding utilities."""

from .constants import (
    DEFAULT_EMBEDDING_DIMENSIONS,
    DEFAULT_EMBEDDING_MODEL,
    MODEL_DIMENSIONS,
    SUPPORTED_EMBEDDING_MODELS,
)
from .exceptions import (
    EmbeddingError,
    InvalidEmbeddingModelError,
    InvalidEmbeddingVectorError,
)
from .operations import (
    default_embedding_model,
    embedding_dimensions,
    supported_embedding_model,
    valid_embedding_vector,
)

__all__ = [
    "DEFAULT_EMBEDDING_DIMENSIONS",
    "DEFAULT_EMBEDDING_MODEL",
    "SUPPORTED_EMBEDDING_MODELS",
    "MODEL_DIMENSIONS",
    "EmbeddingError",
    "InvalidEmbeddingModelError",
    "InvalidEmbeddingVectorError",
    "default_embedding_model",
    "supported_embedding_model",
    "embedding_dimensions",
    "valid_embedding_vector",
]