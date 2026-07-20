from __future__ import annotations

"""Constants for the ai_memory.vector module."""

from __future__ import annotations

from enum import Enum


class VectorType(str, Enum):
    """Supported vector types."""

    DENSE = "dense"
    SPARSE = "sparse"
    HYBRID = "hybrid"


class VectorMetric(str, Enum):
    """Supported similarity metrics."""

    COSINE = "cosine"
    DOT_PRODUCT = "dot_product"
    EUCLIDEAN = "euclidean"


class VectorState(str, Enum):
    """Vector lifecycle states."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"


DEFAULT_VECTOR_DIMENSIONS = 1536
DEFAULT_VECTOR_NAMESPACE = "default"
