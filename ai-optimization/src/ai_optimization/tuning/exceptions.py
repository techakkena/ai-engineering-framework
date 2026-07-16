"""Exceptions for the ai_optimization.tuning module."""

from __future__ import annotations


class TuningError(Exception):
    """Base exception for tuning operations."""


class TuningValidationError(TuningError):
    """Raised when tuning validation fails."""


class TuningRegistrationError(TuningError):
    """Raised when tuning registration fails."""


class TuningNotFoundError(TuningRegistrationError):
    """Raised when a tuning definition cannot be found."""


class DuplicateTuningError(TuningRegistrationError):
    """Raised when attempting to register a duplicate tuning."""


class UnsupportedTuningStrategyError(
    TuningValidationError,
):
    """Raised when an unsupported tuning strategy is specified."""


__all__ = [
    "DuplicateTuningError",
    "TuningError",
    "TuningNotFoundError",
    "TuningRegistrationError",
    "TuningValidationError",
    "UnsupportedTuningStrategyError",
]