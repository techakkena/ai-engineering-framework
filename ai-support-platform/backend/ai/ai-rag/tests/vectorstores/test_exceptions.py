from __future__ import annotations

from ai_rag.vectorstores.exceptions import (
    InvalidDistanceMetricError,
    InvalidVectorStoreError,
    VectorStoreError,
)


def test_vector_store_error():
    assert issubclass(
        VectorStoreError,
        Exception,
    )


def test_invalid_vector_store_error():
    assert issubclass(
        InvalidVectorStoreError,
        VectorStoreError,
    )


def test_invalid_distance_metric_error():
    assert issubclass(
        InvalidDistanceMetricError,
        VectorStoreError,
    )
