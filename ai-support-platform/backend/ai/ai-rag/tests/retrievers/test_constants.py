from __future__ import annotations

from ai_rag.retrievers.constants import (
    DEFAULT_RETRIEVER,
    DEFAULT_TOP_K,
    MAX_TOP_K,
    MIN_TOP_K,
    SUPPORTED_RETRIEVERS,
)


def test_default_retriever():
    assert DEFAULT_RETRIEVER == "similarity"


def test_default_top_k():
    assert DEFAULT_TOP_K == 5


def test_supported_retrievers():
    assert "similarity" in SUPPORTED_RETRIEVERS
    assert "mmr" in SUPPORTED_RETRIEVERS
    assert "hybrid" in SUPPORTED_RETRIEVERS


def test_top_k_limits():
    assert MIN_TOP_K < MAX_TOP_K
