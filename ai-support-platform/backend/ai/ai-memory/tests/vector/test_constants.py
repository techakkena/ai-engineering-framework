from __future__ import annotations

"""Tests for ai_memory.vector.constants."""

from ai_memory.vector.constants import (
    DEFAULT_VECTOR_DIMENSIONS,
    DEFAULT_VECTOR_NAMESPACE,
    VectorMetric,
    VectorState,
    VectorType,
)


def test_vector_type_values() -> None:
    assert VectorType.DENSE.value == "dense"
    assert VectorType.SPARSE.value == "sparse"
    assert VectorType.HYBRID.value == "hybrid"


def test_vector_metric_values() -> None:
    assert VectorMetric.COSINE.value == "cosine"
    assert VectorMetric.DOT_PRODUCT.value == "dot_product"
    assert VectorMetric.EUCLIDEAN.value == "euclidean"


def test_vector_state_values() -> None:
    assert VectorState.ACTIVE.value == "active"
    assert VectorState.INACTIVE.value == "inactive"
    assert VectorState.ARCHIVED.value == "archived"


def test_default_values() -> None:
    assert DEFAULT_VECTOR_DIMENSIONS == 1536
    assert DEFAULT_VECTOR_NAMESPACE == "default"
