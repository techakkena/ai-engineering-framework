from ai_rag.vectorstores.constants import (
    DEFAULT_DISTANCE_METRIC,
    DEFAULT_VECTOR_STORE,
    SUPPORTED_DISTANCE_METRICS,
    SUPPORTED_VECTOR_STORES,
)


def test_default_vector_store():
    assert DEFAULT_VECTOR_STORE == "faiss"


def test_supported_vector_stores():
    assert "faiss" in SUPPORTED_VECTOR_STORES
    assert "qdrant" in SUPPORTED_VECTOR_STORES


def test_default_distance_metric():
    assert DEFAULT_DISTANCE_METRIC == "cosine"


def test_supported_distance_metrics():
    assert "cosine" in SUPPORTED_DISTANCE_METRICS