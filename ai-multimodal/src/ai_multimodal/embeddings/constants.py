"""
Constants for the ai_multimodal.embeddings module.

This module defines framework-independent constants used by embedding
operations throughout the AI Engineering Framework.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Embedding tasks
# ---------------------------------------------------------------------------

TASK_CREATE: Final[str] = "create"
TASK_COMPARE: Final[str] = "compare"
TASK_SEARCH: Final[str] = "search"
TASK_UPDATE: Final[str] = "update"
TASK_METADATA: Final[str] = "metadata"

SUPPORTED_TASKS: Final[tuple[str, ...]] = (
    TASK_CREATE,
    TASK_COMPARE,
    TASK_SEARCH,
    TASK_UPDATE,
    TASK_METADATA,
)

# ---------------------------------------------------------------------------
# Supported embedding types
# ---------------------------------------------------------------------------

EMBEDDING_TYPE_TEXT: Final[str] = "text"
EMBEDDING_TYPE_IMAGE: Final[str] = "image"
EMBEDDING_TYPE_AUDIO: Final[str] = "audio"
EMBEDDING_TYPE_VIDEO: Final[str] = "video"
EMBEDDING_TYPE_DOCUMENT: Final[str] = "document"

SUPPORTED_EMBEDDING_TYPES: Final[tuple[str, ...]] = (
    EMBEDDING_TYPE_TEXT,
    EMBEDDING_TYPE_IMAGE,
    EMBEDDING_TYPE_AUDIO,
    EMBEDDING_TYPE_VIDEO,
    EMBEDDING_TYPE_DOCUMENT,
)

# ---------------------------------------------------------------------------
# Vector configuration
# ---------------------------------------------------------------------------

DEFAULT_VECTOR_DIMENSIONS: Final[int] = 1536
MAX_VECTOR_DIMENSIONS: Final[int] = 8192

DEFAULT_TOP_K: Final[int] = 10
MAX_TOP_K: Final[int] = 1000

# ---------------------------------------------------------------------------
# Similarity metrics
# ---------------------------------------------------------------------------

SIMILARITY_COSINE: Final[str] = "cosine"
SIMILARITY_DOT_PRODUCT: Final[str] = "dot_product"
SIMILARITY_EUCLIDEAN: Final[str] = "euclidean"

SUPPORTED_SIMILARITY_METRICS: Final[tuple[str, ...]] = (
    SIMILARITY_COSINE,
    SIMILARITY_DOT_PRODUCT,
    SIMILARITY_EUCLIDEAN,
)

# ---------------------------------------------------------------------------
# Confidence
# ---------------------------------------------------------------------------

DEFAULT_SIMILARITY_THRESHOLD: Final[float] = 0.75
MIN_SIMILARITY_THRESHOLD: Final[float] = 0.0
MAX_SIMILARITY_THRESHOLD: Final[float] = 1.0

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_PROVIDER: Final[str] = "provider"
METADATA_MODEL: Final[str] = "model"
METADATA_DIMENSIONS: Final[str] = "dimensions"
METADATA_METRIC: Final[str] = "similarity_metric"
METADATA_LATENCY: Final[str] = "latency_ms"