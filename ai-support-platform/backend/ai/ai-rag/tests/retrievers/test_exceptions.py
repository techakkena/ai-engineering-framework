from __future__ import annotations

from ai_rag.retrievers.exceptions import (
    InvalidRetrieverError,
    InvalidTopKError,
    RetrieverError,
)


def test_retriever_error():
    assert issubclass(
        RetrieverError,
        Exception,
    )


def test_invalid_retriever_error():
    assert issubclass(
        InvalidRetrieverError,
        RetrieverError,
    )


def test_invalid_top_k_error():
    assert issubclass(
        InvalidTopKError,
        RetrieverError,
    )
