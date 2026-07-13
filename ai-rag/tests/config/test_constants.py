from ai_rag.config.constants import (
    DEFAULT_CHUNK_OVERLAP,
    DEFAULT_CHUNK_SIZE,
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_RERANKER,
    DEFAULT_RETRIEVER,
    DEFAULT_TOP_K,
    DEFAULT_VECTOR_STORE,
)


def test_chunk_size():
    assert DEFAULT_CHUNK_SIZE == 1000


def test_chunk_overlap():
    assert DEFAULT_CHUNK_OVERLAP == 200


def test_embedding_model():
    assert DEFAULT_EMBEDDING_MODEL == "text-embedding-3-small"


def test_vector_store():
    assert DEFAULT_VECTOR_STORE == "faiss"


def test_retriever():
    assert DEFAULT_RETRIEVER == "similarity"


def test_reranker():
    assert DEFAULT_RERANKER == "cross-encoder"


def test_top_k():
    assert DEFAULT_TOP_K == 5