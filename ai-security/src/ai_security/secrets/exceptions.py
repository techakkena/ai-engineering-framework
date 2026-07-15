"""
Exceptions for the secrets module.
"""

from __future__ import annotations


class SecretError(Exception):
    """Base exception for secret operations."""


class SecretConfigurationError(SecretError):
    """Raised when the secret manager is improperly configured."""


class SecretGenerationError(SecretError):
    """Raised when a secret cannot be generated."""


class SecretNotFoundError(SecretError):
    """Raised when a requested secret cannot be found."""