"""Exceptions for the ai_analytics.events module."""

from __future__ import annotations


class EventError(Exception):
    """Base exception for event operations."""


class EventValidationError(EventError):
    """Raised when event validation fails."""


class EventRegistrationError(EventError):
    """Raised when event registration fails."""


class EventNotFoundError(EventRegistrationError):
    """Raised when a requested event cannot be found."""


class DuplicateEventError(EventRegistrationError):
    """Raised when attempting to register a duplicate event."""


class UnsupportedEventTypeError(EventValidationError):
    """Raised when an unsupported event type is specified."""


__all__ = [
    "DuplicateEventError",
    "EventError",
    "EventNotFoundError",
    "EventRegistrationError",
    "EventValidationError",
    "UnsupportedEventTypeError",
]