"""Exceptions for rerankers."""


class RerankerError(Exception):
    """Base reranker exception."""


class InvalidRerankerError(RerankerError):
    """Raised when a reranker is unsupported."""


class InvalidTopKError(RerankerError):
    """Raised when top_k is invalid."""