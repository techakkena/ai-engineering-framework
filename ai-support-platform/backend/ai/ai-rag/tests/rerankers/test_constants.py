from __future__ import annotations

from ai_rag.rerankers.constants import (
    DEFAULT_RERANKER,
    DEFAULT_TOP_K,
    MAX_TOP_K,
    MIN_TOP_K,
    SUPPORTED_RERANKERS,
)


def test_default_reranker():
    assert DEFAULT_RERANKER == "cross-encoder"


def test_default_top_k():
    assert DEFAULT_TOP_K == 10


def test_supported_rerankers():
    assert "cross-encoder" in SUPPORTED_RERANKERS
    assert "cohere" in SUPPORTED_RERANKERS


def test_top_k_limits():
    assert MIN_TOP_K < MAX_TOP_K
