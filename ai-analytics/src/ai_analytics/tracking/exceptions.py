"""Exceptions for the ai_analytics.tracking module."""

from __future__ import annotations


class TrackingError(Exception):
    """Base exception for tracking operations."""


class TrackingValidationError(TrackingError):
    """Raised when tracking validation fails."""


class TrackingRegistrationError(TrackingError):
    """Raised when tracking registration fails."""


class TrackingNotFoundError(TrackingRegistrationError):
    """Raised when a tracking definition cannot be found."""


class DuplicateTrackingError(TrackingRegistrationError):
    """Raised when attempting to register a duplicate tracking definition."""


class UnsupportedTrackingTypeError(TrackingValidationError):
    """Raised when an unsupported tracking type is supplied."""


__all__ = [
    "DuplicateTrackingError",
    "TrackingError",
    "TrackingNotFoundError",
    "TrackingRegistrationError",
    "TrackingValidationError",
    "UnsupportedTrackingTypeError",
]