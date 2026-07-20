from __future__ import annotations

from ai_rag.retrievers.operations import (
    default_retriever,
    default_top_k,
    supported_retriever,
    validate_top_k,
)


def test_default_retriever():
    assert default_retriever() == "similarity"


def test_supported_retriever():
    assert supported_retriever("similarity")


def test_unsupported_retriever():
    assert not supported_retriever("unknown")


def test_default_top_k():
    assert default_top_k() == 5


def test_valid_top_k():
    assert validate_top_k(10)


def test_invalid_top_k_low():
    assert not validate_top_k(0)


def test_invalid_top_k_high():
    assert not validate_top_k(1000)
