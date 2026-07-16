"""Exceptions for the ai_optimization.scheduling module."""

from __future__ import annotations


class ScheduleError(Exception):
    """Base exception for scheduling operations."""


class ScheduleValidationError(ScheduleError):
    """Raised when schedule validation fails."""


class ScheduleRegistrationError(ScheduleError):
    """Raised when schedule registration fails."""


class ScheduleNotFoundError(
    ScheduleRegistrationError,
):
    """Raised when a schedule definition cannot be found."""


class DuplicateScheduleError(
    ScheduleRegistrationError,
):
    """Raised when attempting to register a duplicate schedule."""


class UnsupportedSchedulerError(
    ScheduleValidationError,
):
    """Raised when an unsupported scheduler is specified."""


__all__ = [
    "DuplicateScheduleError",
    "ScheduleError",
    "ScheduleNotFoundError",
    "ScheduleRegistrationError",
    "ScheduleValidationError",
    "UnsupportedSchedulerError",
]