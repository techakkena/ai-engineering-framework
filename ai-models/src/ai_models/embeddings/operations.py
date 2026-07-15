"""
Operations for ai_models.embeddings.
"""

from __future__ import annotations

import re
import uuid

from ai_models.embeddings.constants import (
    SUPPORTED_EMBEDDING_PROVIDERS,
)
from ai_models.embeddings.exceptions import (
    InvalidEmbeddingProviderError,
)


def normalize_embedding_provider(
    provider: str,
) -> str:
    """
    Normalize an embedding provider.
    """
    return provider.strip().lower()


def validate_embedding_provider(
    provider: str,
) -> str:
    """
    Validate an embedding provider.
    """
    normalized = normalize_embedding_provider(
        provider,
    )

    if (
        normalized
        not in SUPPORTED_EMBEDDING_PROVIDERS
    ):
        raise InvalidEmbeddingProviderError(
            provider,
        )

    return normalized


def is_supported_embedding_provider(
    provider: str,
) -> bool:
    """
    Determine whether an embedding provider
    is supported.
    """
    return (
        normalize_embedding_provider(
            provider,
        )
        in SUPPORTED_EMBEDDING_PROVIDERS
    )


def validate_embedding_id(
    embedding_id: str,
) -> str:
    """
    Validate an embedding identifier.
    """
    normalized = embedding_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            "Invalid embedding identifier: "
            f"'{embedding_id}'."
        )

    return normalized


def build_embedding_id() -> str:
    """
    Build a unique embedding identifier.
    """
    return (
        f"embedding-{uuid.uuid4()}"
    )