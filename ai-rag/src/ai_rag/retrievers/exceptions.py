"""Exceptions for retrievers."""


class RetrieverError(Exception):
    """Base retriever exception."""


class InvalidRetrieverError(RetrieverError):
    """Raised when a retriever type is unsupported."""


class InvalidTopKError(RetrieverError):
    """Raised when top_k is invalid."""