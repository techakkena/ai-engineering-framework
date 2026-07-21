from __future__ import annotations

from ai_rag.embeddings.operations import (
    default_embedding_model,
    embedding_dimensions,
    supported_embedding_model,
    valid_embedding_vector,
)


def test_default_model():
    assert default_embedding_model() == "text-embedding-3-small"


def test_supported_model():
    assert supported_embedding_model("text-embedding-3-small")


def test_unsupported_model():
    assert not supported_embedding_model("unknown-model")


def test_embedding_dimensions():
    assert embedding_dimensions("text-embedding-3-large") == 3072


def test_default_dimensions():
    assert embedding_dimensions("unknown") == 1536


def test_valid_vector():
    assert valid_embedding_vector([1.0, 2.0, 3.0])


def test_invalid_vector():
    assert not valid_embedding_vector([])


def test_invalid_vector_types():
    assert not valid_embedding_vector([1.0, "abc"])  # type: ignore[list-item]
