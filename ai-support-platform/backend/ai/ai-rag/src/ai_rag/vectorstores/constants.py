from __future__ import annotations

"""Constants for vector stores."""

DEFAULT_VECTOR_STORE = "faiss"

SUPPORTED_VECTOR_STORES = (
    "faiss",
    "chroma",
    "pinecone",
    "qdrant",
    "milvus",
    "weaviate",
    "pgvector",
)

DEFAULT_DISTANCE_METRIC = "cosine"

SUPPORTED_DISTANCE_METRICS = (
    "cosine",
    "euclidean",
    "dot",
)
