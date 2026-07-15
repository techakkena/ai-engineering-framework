"""
Operations for ai_security.encryption.
"""

from __future__ import annotations

import re
import uuid

from ai_security.encryption.constants import (
    SUPPORTED_ENCRYPTION_PROVIDERS,
)
from ai_security.encryption.exceptions import (
    InvalidEncryptionProviderError,
)


def normalize_encryption_provider(
    provider: str,
) -> str:
    """
    Normalize an encryption provider.

    Args:
        provider:
            Provider name.

    Returns:
        Normalized provider.
    """
    return provider.strip().lower()


def validate_encryption_provider(
    provider: str,
) -> str:
    """
    Validate an encryption provider.

    Args:
        provider:
            Provider name.

    Returns:
        Normalized provider.

    Raises:
        InvalidEncryptionProviderError:
            If the provider is unsupported.
    """
    normalized = (
        normalize_encryption_provider(
            provider,
        )
    )

    if (
        normalized
        not in SUPPORTED_ENCRYPTION_PROVIDERS
    ):
        raise InvalidEncryptionProviderError(
            provider,
        )

    return normalized


def is_supported_encryption_provider(
    provider: str,
) -> bool:
    """
    Determine whether an encryption provider
    is supported.

    Args:
        provider:
            Provider name.

    Returns:
        True if supported.
    """
    return (
        normalize_encryption_provider(
            provider,
        )
        in SUPPORTED_ENCRYPTION_PROVIDERS
    )


def validate_encryption_id(
    encryption_id: str,
) -> str:
    """
    Validate an encryption identifier.

    Args:
        encryption_id:
            Identifier to validate.

    Returns:
        Normalized identifier.

    Raises:
        ValueError:
            If the identifier is invalid.
    """
    normalized = (
        encryption_id.strip().lower()
    )

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            (
                "Invalid encryption "
                f"identifier: "
                f"'{encryption_id}'."
            )
        )

    return normalized


def build_encryption_id() -> str:
    """
    Build a unique encryption identifier.

    Returns:
        A unique encryption identifier.
    """
    return (
        f"encryption-{uuid.uuid4()}"
    )