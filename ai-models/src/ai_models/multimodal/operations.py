"""
Operations for ai_models.multimodal.
"""

from __future__ import annotations

import re
import uuid

from ai_models.multimodal.constants import (
    SUPPORTED_MULTIMODAL_PROVIDERS,
)
from ai_models.multimodal.exceptions import (
    InvalidMultimodalProviderError,
)


def normalize_multimodal_provider(
    provider: str,
) -> str:
    """
    Normalize a multimodal provider.

    Args:
        provider:
            Provider name.

    Returns:
        Normalized provider name.
    """
    return provider.strip().lower()


def validate_multimodal_provider(
    provider: str,
) -> str:
    """
    Validate a multimodal provider.

    Args:
        provider:
            Provider name.

    Returns:
        Normalized provider.

    Raises:
        InvalidMultimodalProviderError:
            If the provider is unsupported.
    """
    normalized = normalize_multimodal_provider(
        provider,
    )

    if (
        normalized
        not in SUPPORTED_MULTIMODAL_PROVIDERS
    ):
        raise InvalidMultimodalProviderError(
            provider,
        )

    return normalized


def is_supported_multimodal_provider(
    provider: str,
) -> bool:
    """
    Determine whether a provider is supported.

    Args:
        provider:
            Provider name.

    Returns:
        True if supported.
    """
    return (
        normalize_multimodal_provider(
            provider,
        )
        in SUPPORTED_MULTIMODAL_PROVIDERS
    )


def validate_multimodal_id(
    multimodal_id: str,
) -> str:
    """
    Validate a multimodal identifier.

    Args:
        multimodal_id:
            Identifier to validate.

    Returns:
        Normalized identifier.

    Raises:
        ValueError:
            If the identifier is invalid.
    """
    normalized = (
        multimodal_id.strip().lower()
    )

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            (
                "Invalid multimodal "
                f"identifier: "
                f"'{multimodal_id}'."
            )
        )

    return normalized


def build_multimodal_id() -> str:
    """
    Build a unique multimodal identifier.

    Returns:
        A unique multimodal identifier.
    """
    return (
        f"multimodal-{uuid.uuid4()}"
    )