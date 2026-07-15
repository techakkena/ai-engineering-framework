"""
Operations for ai_models.registry.
"""

from __future__ import annotations

import re
import uuid

from ai_models.registry.constants import (
    SUPPORTED_REGISTRY_PROVIDERS,
)
from ai_models.registry.exceptions import (
    InvalidRegistryProviderError,
)


def normalize_registry_provider(
    provider: str,
) -> str:
    """
    Normalize a registry provider.
    """
    return provider.strip().lower()


def validate_registry_provider(
    provider: str,
) -> str:
    """
    Validate a registry provider.
    """
    normalized = normalize_registry_provider(
        provider,
    )

    if (
        normalized
        not in SUPPORTED_REGISTRY_PROVIDERS
    ):
        raise InvalidRegistryProviderError(
            provider,
        )

    return normalized


def is_supported_registry_provider(
    provider: str,
) -> bool:
    """
    Determine whether a registry provider
    is supported.
    """
    return (
        normalize_registry_provider(
            provider,
        )
        in SUPPORTED_REGISTRY_PROVIDERS
    )


def validate_registry_id(
    registry_id: str,
) -> str:
    """
    Validate a registry identifier.
    """
    normalized = registry_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            (
                "Invalid registry "
                f"identifier: "
                f"'{registry_id}'."
            )
        )

    return normalized


def build_registry_id() -> str:
    """
    Build a unique registry identifier.
    """
    return (
        f"registry-{uuid.uuid4()}"
    )