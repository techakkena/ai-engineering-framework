"""Exceptions for the ai_cloud.networking module."""

from __future__ import annotations


class NetworkError(Exception):
    """Base exception for network operations."""


class NetworkValidationError(NetworkError):
    """Raised when network validation fails."""


class NetworkRegistrationError(NetworkError):
    """Raised when network registration fails."""


class NetworkNotFoundError(
    NetworkRegistrationError,
):
    """Raised when a network definition cannot be found."""


class DuplicateNetworkError(
    NetworkRegistrationError,
):
    """Raised when attempting to register a duplicate network."""


class UnsupportedNetworkTypeError(
    NetworkValidationError,
):
    """Raised when an unsupported network type is specified."""


__all__ = [
    "DuplicateNetworkError",
    "NetworkError",
    "NetworkNotFoundError",
    "NetworkRegistrationError",
    "NetworkValidationError",
    "UnsupportedNetworkTypeError",
]