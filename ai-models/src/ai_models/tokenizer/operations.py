"""
Operations for ai_models.tokenizer.
"""

from __future__ import annotations

import re
import uuid

from ai_models.tokenizer.constants import (
    SUPPORTED_TOKENIZER_PROVIDERS,
)
from ai_models.tokenizer.exceptions import (
    InvalidTokenizerProviderError,
)


def normalize_tokenizer_provider(
    provider: str,
) -> str:
    """
    Normalize a tokenizer provider.

    Args:
        provider:
            Provider name.

    Returns:
        Normalized provider name.
    """
    return provider.strip().lower()


def validate_tokenizer_provider(
    provider: str,
) -> str:
    """
    Validate a tokenizer provider.

    Args:
        provider:
            Provider name.

    Returns:
        Normalized provider.

    Raises:
        InvalidTokenizerProviderError:
            If the provider is unsupported.
    """
    normalized = (
        normalize_tokenizer_provider(
            provider,
        )
    )

    if (
        normalized
        not in SUPPORTED_TOKENIZER_PROVIDERS
    ):
        raise InvalidTokenizerProviderError(
            provider,
        )

    return normalized


def is_supported_tokenizer_provider(
    provider: str,
) -> bool:
    """
    Determine whether a tokenizer provider
    is supported.

    Args:
        provider:
            Provider name.

    Returns:
        True if supported.
    """
    return (
        normalize_tokenizer_provider(
            provider,
        )
        in SUPPORTED_TOKENIZER_PROVIDERS
    )


def validate_tokenizer_id(
    tokenizer_id: str,
) -> str:
    """
    Validate a tokenizer identifier.

    Args:
        tokenizer_id:
            Identifier to validate.

    Returns:
        Normalized identifier.

    Raises:
        ValueError:
            If the identifier is invalid.
    """
    normalized = (
        tokenizer_id.strip().lower()
    )

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            (
                "Invalid tokenizer "
                f"identifier: "
                f"'{tokenizer_id}'."
            )
        )

    return normalized


def build_tokenizer_id() -> str:
    """
    Build a unique tokenizer identifier.

    Returns:
        Unique tokenizer identifier.
    """
    return (
        f"tokenizer-{uuid.uuid4()}"
    )