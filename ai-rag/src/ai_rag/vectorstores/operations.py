"""Operations for vector stores."""

from .constants import (
    DEFAULT_DISTANCE_METRIC,
    DEFAULT_VECTOR_STORE,
    SUPPORTED_DISTANCE_METRICS,
    SUPPORTED_VECTOR_STORES,
)


def default_vector_store() -> str:
    """Return the default vector store."""

    return DEFAULT_VECTOR_STORE


def supported_vector_store(store: str) -> bool:
    """Return True if the vector store is supported."""

    return store.lower() in SUPPORTED_VECTOR_STORES


def default_distance_metric() -> str:
    """Return the default distance metric."""

    return DEFAULT_DISTANCE_METRIC


def supported_distance_metric(metric: str) -> bool:
    """Return True if the distance metric is supported."""

    return metric.lower() in SUPPORTED_DISTANCE_METRICS