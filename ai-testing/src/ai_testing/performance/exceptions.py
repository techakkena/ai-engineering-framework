"""Exceptions for the ai_testing.performance module."""

from __future__ import annotations


class PerformanceError(Exception):
    """Base exception for performance operations."""


class PerformanceValidationError(PerformanceError):
    """Raised when benchmark configuration is invalid."""


class InvalidIterationCountError(PerformanceValidationError):
    """Raised when the iteration count is invalid."""


class UnsupportedTimeUnitError(PerformanceValidationError):
    """Raised when an unsupported time unit is supplied."""


__all__ = [
    "InvalidIterationCountError",
    "PerformanceError",
    "PerformanceValidationError",
    "UnsupportedTimeUnitError",
]