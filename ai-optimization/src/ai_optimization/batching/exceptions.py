"""Exceptions for the ai_optimization.batching module."""

from __future__ import annotations


class BatchError(Exception):
    """Base exception for batch operations."""


class BatchValidationError(BatchError):
    """Raised when batch validation fails."""


class BatchRegistrationError(BatchError):
    """Raised when batch registration fails."""


class BatchNotFoundError(BatchRegistrationError):
    """Raised when a requested batch cannot be found."""


class DuplicateBatchError(BatchRegistrationError):
    """Raised when attempting to register a duplicate batch."""


class UnsupportedBatchStrategyError(
    BatchValidationError,
):
    """Raised when an unsupported batching strategy is specified."""


__all__ = [
    "BatchError",
    "BatchNotFoundError",
    "BatchRegistrationError",
    "BatchValidationError",
    "DuplicateBatchError",
    "UnsupportedBatchStrategyError",
]