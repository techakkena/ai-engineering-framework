"""Exceptions for the ai_testing.snapshots module."""

from __future__ import annotations


class SnapshotError(Exception):
    """Base exception for snapshot operations."""


class SnapshotValidationError(SnapshotError):
    """Raised when snapshot validation fails."""


class SnapshotRegistrationError(SnapshotError):
    """Raised when snapshot registration fails."""


class SnapshotNotFoundError(SnapshotRegistrationError):
    """Raised when a snapshot cannot be found."""


class DuplicateSnapshotError(SnapshotRegistrationError):
    """Raised when attempting to register a duplicate snapshot."""


class UnsupportedSnapshotFormatError(SnapshotValidationError):
    """Raised when an unsupported snapshot format is specified."""


__all__ = [
    "DuplicateSnapshotError",
    "SnapshotError",
    "SnapshotNotFoundError",
    "SnapshotRegistrationError",
    "SnapshotValidationError",
    "UnsupportedSnapshotFormatError",
]