"""Vector store utilities."""

from .constants import (
    DEFAULT_DISTANCE_METRIC,
    DEFAULT_VECTOR_STORE,
    SUPPORTED_DISTANCE_METRICS,
    SUPPORTED_VECTOR_STORES,
)
from .exceptions import (
    InvalidDistanceMetricError,
    InvalidVectorStoreError,
    VectorStoreError,
)
from .operations import (
    default_distance_metric,
    default_vector_store,
    supported_distance_metric,
    supported_vector_store,
)

__all__ = [
    "DEFAULT_DISTANCE_METRIC",
    "DEFAULT_VECTOR_STORE",
    "SUPPORTED_DISTANCE_METRICS",
    "SUPPORTED_VECTOR_STORES",
    "VectorStoreError",
    "InvalidVectorStoreError",
    "InvalidDistanceMetricError",
    "default_vector_store",
    "supported_vector_store",
    "default_distance_metric",
    "supported_distance_metric",
]