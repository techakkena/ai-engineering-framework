from __future__ import annotations

"""Constants for ai-rag configuration."""

DEFAULT_CHUNK_SIZE = 1000

DEFAULT_CHUNK_OVERLAP = 200

DEFAULT_EMBEDDING_MODEL = "text-embedding-3-small"

DEFAULT_VECTOR_STORE = "faiss"

DEFAULT_RETRIEVER = "similarity"

DEFAULT_TOP_K = 5

DEFAULT_RERANKER = "cross-encoder"
