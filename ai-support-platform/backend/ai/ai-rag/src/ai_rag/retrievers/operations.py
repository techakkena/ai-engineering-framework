from __future__ import annotations

"""Operations for retrievers."""

from .constants import (
    DEFAULT_RETRIEVER,
    DEFAULT_TOP_K,
    MAX_TOP_K,
    MIN_TOP_K,
    SUPPORTED_RETRIEVERS,
)


def default_retriever() -> str:
    """Return the default retriever."""

    return DEFAULT_RETRIEVER


def supported_retriever(name: str) -> bool:
    """Return True if the retriever is supported."""

    return name.lower() in SUPPORTED_RETRIEVERS


def validate_top_k(value: int) -> bool:
    """Validate top_k."""

    return MIN_TOP_K <= value <= MAX_TOP_K


def default_top_k() -> int:
    """Return the default retrieval count."""

    return DEFAULT_TOP_K
