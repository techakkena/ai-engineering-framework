"""Exceptions for the ai_cloud.providers module."""

from __future__ import annotations


class ProviderError(Exception):
    """Base exception for provider operations."""


class ProviderValidationError(ProviderError):
    """Raised when provider validation fails."""


class ProviderRegistrationError(ProviderError):
    """Raised when provider registration fails."""


class ProviderNotFoundError(
    ProviderRegistrationError,
):
    """Raised when a provider cannot be found."""


class DuplicateProviderError(
    ProviderRegistrationError,
):
    """Raised when attempting to register a duplicate provider."""


class UnsupportedProviderTypeError(
    ProviderValidationError,
):
    """Raised when an unsupported provider type is specified."""


__all__ = [
    "DuplicateProviderError",
    "ProviderError",
    "ProviderNotFoundError",
    "ProviderRegistrationError",
    "ProviderValidationError",
    "UnsupportedProviderTypeError",
]