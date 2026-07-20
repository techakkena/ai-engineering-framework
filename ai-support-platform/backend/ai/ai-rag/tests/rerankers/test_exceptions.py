from __future__ import annotations

from ai_rag.rerankers.exceptions import (
    InvalidRerankerError,
    InvalidTopKError,
    RerankerError,
)


def test_reranker_error():
    assert issubclass(
        RerankerError,
        Exception,
    )


def test_invalid_reranker_error():
    assert issubclass(
        InvalidRerankerError,
        RerankerError,
    )


def test_invalid_top_k_error():
    assert issubclass(
        InvalidTopKError,
        RerankerError,
    )
