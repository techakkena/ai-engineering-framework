from __future__ import annotations

"""Exceptions for vector stores."""


class VectorStoreError(Exception):
    """Base vector store exception."""


class InvalidVectorStoreError(VectorStoreError):
    """Raised when a vector store is unsupported."""


class InvalidDistanceMetricError(VectorStoreError):
    """Raised when a distance metric is unsupported."""
