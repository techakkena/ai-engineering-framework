"""Exceptions for the ai_plugins.discovery module."""

from __future__ import annotations


class DiscoveryError(Exception):
    """Base exception for discovery operations."""


class DiscoveryValidationError(DiscoveryError):
    """Raised when discovery validation fails."""


class DiscoveryRegistrationError(DiscoveryError):
    """Raised when discovery registration fails."""


class DiscoveryNotFoundError(
    DiscoveryRegistrationError,
):
    """Raised when a discovery definition cannot be found."""


class DuplicateDiscoveryError(
    DiscoveryRegistrationError,
):
    """Raised when attempting to register a duplicate discovery."""


class UnsupportedDiscoveryStrategyError(
    DiscoveryValidationError,
):
    """Raised when an unsupported discovery strategy is specified."""


__all__ = [
    "DiscoveryError",
    "DiscoveryNotFoundError",
    "DiscoveryRegistrationError",
    "DiscoveryValidationError",
    "DuplicateDiscoveryError",
    "UnsupportedDiscoveryStrategyError",
]