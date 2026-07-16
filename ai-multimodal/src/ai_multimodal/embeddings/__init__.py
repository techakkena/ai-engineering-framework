"""
ai_multimodal.embeddings

Enterprise embeddings module for the AI Engineering Framework.

This package provides provider-independent abstractions for generating,
managing, comparing, and searching vector embeddings for text, images,
audio, video, and documents.

Modules
-------
constants
    Embedding-related constants and defaults.

exceptions
    Embedding-specific exception hierarchy.

operations
    High-level embedding operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_multimodal.embeddings.operations import (
    compare_embeddings,
    create_embedding,
    get_embedding_metadata,
    search_similar_embeddings,
    update_embedding,
)

__all__ = [
    "create_embedding",
    "compare_embeddings",
    "search_similar_embeddings",
    "update_embedding",
    "get_embedding_metadata",
]