from __future__ import annotations

"""
AI Engineering Framework
Embedding Models Tests

Author : TECHAKKENA
"""

from ai.providers.models import EmbeddingModels


def test_embedding_small():
    assert EmbeddingModels.TEXT_EMBEDDING_3_SMALL.value == "text-embedding-3-small"


def test_embedding_large():
    assert EmbeddingModels.TEXT_EMBEDDING_3_LARGE.value == "text-embedding-3-large"


def test_embedding_ada():
    assert EmbeddingModels.TEXT_EMBEDDING_ADA_002.value == "text-embedding-ada-002"
