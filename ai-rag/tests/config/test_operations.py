from ai_rag.config.operations import (
    default_chunk_overlap,
    default_chunk_size,
    default_embedding_model,
    default_reranker,
    default_retriever,
    default_top_k,
    default_vector_store,
)


def test_default_chunk_size():
    assert default_chunk_size() == 1000


def test_default_chunk_overlap():
    assert default_chunk_overlap() == 200


def test_default_embedding_model():
    assert default_embedding_model() == "text-embedding-3-small"


def test_default_vector_store():
    assert default_vector_store() == "faiss"


def test_default_retriever():
    assert default_retriever() == "similarity"


def test_default_reranker():
    assert default_reranker() == "cross-encoder"


def test_default_top_k():
    assert default_top_k() == 5