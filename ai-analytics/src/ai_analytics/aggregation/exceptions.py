"""Exceptions for the ai_analytics.aggregation module."""

from __future__ import annotations


class AggregationError(Exception):
    """Base exception for aggregation operations."""


class AggregationValidationError(AggregationError):
    """Raised when aggregation validation fails."""


class AggregationRegistrationError(AggregationError):
    """Raised when aggregation registration fails."""


class AggregationNotFoundError(AggregationRegistrationError):
    """Raised when an aggregation cannot be found."""


class DuplicateAggregationError(AggregationRegistrationError):
    """Raised when attempting to register a duplicate aggregation."""


class UnsupportedAggregationTypeError(
    AggregationValidationError,
):
    """Raised when an unsupported aggregation type is supplied."""


__all__ = [
    "AggregationError",
    "AggregationNotFoundError",
    "AggregationRegistrationError",
    "AggregationValidationError",
    "DuplicateAggregationError",
    "UnsupportedAggregationTypeError",
]