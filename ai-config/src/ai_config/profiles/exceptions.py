"""
Custom exceptions for the profiles module.

Author: TECHAKKENA
"""


class ProfileError(Exception):
    """Base exception for profile operations."""


class ProfileNotFoundError(ProfileError):
    """Raised when a profile does not exist."""


class DuplicateProfileError(ProfileError):
    """Raised when a profile already exists."""


class InvalidProfileError(ProfileError):
    """Raised when a profile name is invalid."""
