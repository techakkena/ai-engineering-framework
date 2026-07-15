"""
ai_models.registry

Framework-independent model registry utilities.

This module provides reusable constants, exceptions, and helper
operations for registering and discovering AI models.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_models.registry.constants import (
    DEFAULT_REGISTRY_NAME,
    DEFAULT_REGISTRY_PROVIDER,
    DEFAULT_REGISTRY_VERSION,
    SUPPORTED_REGISTRY_PROVIDERS,
)
from ai_models.registry.exceptions import (
    InvalidRegistryProviderError,
    RegistryConfigurationError,
    RegistryError,
    RegistryValidationError,
)
from ai_models.registry.operations import (
    build_registry_id,
    is_supported_registry_provider,
    normalize_registry_provider,
    validate_registry_id,
    validate_registry_provider,
)

__all__ = [
    "DEFAULT_REGISTRY_NAME",
    "DEFAULT_REGISTRY_PROVIDER",
    "DEFAULT_REGISTRY_VERSION",
    "SUPPORTED_REGISTRY_PROVIDERS",
    "RegistryError",
    "InvalidRegistryProviderError",
    "RegistryConfigurationError",
    "RegistryValidationError",
    "build_registry_id",
    "is_supported_registry_provider",
    "normalize_registry_provider",
    "validate_registry_id",
    "validate_registry_provider",
]