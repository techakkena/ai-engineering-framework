from ai_rag.rerankers.operations import (
    default_reranker,
    default_top_k,
    supported_reranker,
    validate_top_k,
)


def test_default_reranker():
    assert default_reranker() == "cross-encoder"


def test_default_top_k():
    assert default_top_k() == 10


def test_supported_reranker():
    assert supported_reranker("cohere")


def test_unsupported_reranker():
    assert not supported_reranker("unknown")


def test_valid_top_k():
    assert validate_top_k(20)


def test_invalid_top_k_low():
    assert not validate_top_k(0)


def test_invalid_top_k_high():
    assert not validate_top_k(500)