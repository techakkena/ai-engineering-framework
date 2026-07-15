"""
Operations for ai_models.chat.
"""

from __future__ import annotations

import re
import uuid

from ai_models.chat.constants import (
    SUPPORTED_CHAT_PROVIDERS,
)
from ai_models.chat.exceptions import (
    InvalidChatProviderError,
)


def normalize_chat_provider(
    provider: str,
) -> str:
    """
    Normalize a provider name.
    """
    return provider.strip().lower()


def validate_chat_provider(
    provider: str,
) -> str:
    """
    Validate a chat provider.
    """
    normalized = normalize_chat_provider(provider)

    if normalized not in SUPPORTED_CHAT_PROVIDERS:
        raise InvalidChatProviderError(provider)

    return normalized


def is_supported_chat_provider(
    provider: str,
) -> bool:
    """
    Determine whether a provider is supported.
    """
    return (
        normalize_chat_provider(provider)
        in SUPPORTED_CHAT_PROVIDERS
    )


def validate_chat_id(
    chat_id: str,
) -> str:
    """
    Validate a chat identifier.
    """
    normalized = chat_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            f"Invalid chat identifier: '{chat_id}'."
        )

    return normalized


def build_chat_id() -> str:
    """
    Build a unique chat identifier.
    """
    return f"chat-{uuid.uuid4()}"