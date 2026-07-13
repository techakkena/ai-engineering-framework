"""Operations for rerankers."""

from .constants import (
    DEFAULT_RERANKER,
    DEFAULT_TOP_K,
    MAX_TOP_K,
    MIN_TOP_K,
    SUPPORTED_RERANKERS,
)


def default_reranker() -> str:
    """Return the default reranker."""

    return DEFAULT_RERANKER


def default_top_k() -> int:
    """Return the default reranking count."""

    return DEFAULT_TOP_K


def supported_reranker(name: str) -> bool:
    """Return True if the reranker is supported."""

    return name.lower() in SUPPORTED_RERANKERS


def validate_top_k(value: int) -> bool:
    """Validate top_k."""

    return MIN_TOP_K <= value <= MAX_TOP_K