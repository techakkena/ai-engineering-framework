"""Exceptions for indexing."""


class IndexingError(Exception):
    """Base indexing exception."""


class InvalidIndexNameError(IndexingError):
    """Raised when an index name is invalid."""


class InvalidBatchSizeError(IndexingError):
    """Raised when a batch size is invalid."""