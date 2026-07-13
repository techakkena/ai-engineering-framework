from ai_rag.vectorstores.operations import (
    default_distance_metric,
    default_vector_store,
    supported_distance_metric,
    supported_vector_store,
)


def test_default_vector_store():
    assert default_vector_store() == "faiss"


def test_supported_vector_store():
    assert supported_vector_store("faiss")


def test_unsupported_vector_store():
    assert not supported_vector_store("unknown")


def test_default_distance_metric():
    assert default_distance_metric() == "cosine"


def test_supported_distance_metric():
    assert supported_distance_metric("cosine")


def test_unsupported_distance_metric():
    assert not supported_distance_metric("manhattan")