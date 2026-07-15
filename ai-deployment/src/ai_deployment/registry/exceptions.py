"""
Exceptions for the registry module.
"""

from __future__ import annotations


class RegistryError(Exception):
    """Base exception for registry operations."""


class RegistryConfigurationError(RegistryError):
    """Raised when registry configuration is invalid."""


class RegistryOperationError(RegistryError):
    """Raised when a registry operation fails."""