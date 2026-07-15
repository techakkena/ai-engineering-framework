"""
Operations for ai_models.vision.
"""

from __future__ import annotations

import re
import uuid

from ai_models.vision.constants import (
    SUPPORTED_VISION_PROVIDERS,
)
from ai_models.vision.exceptions import (
    InvalidVisionProviderError,
)


def normalize_vision_provider(
    provider: str,
) -> str:
    """
    Normalize a vision provider.
    """
    return provider.strip().lower()


def validate_vision_provider(
    provider: str,
) -> str:
    """
    Validate a vision provider.
    """
    normalized = normalize_vision_provider(
        provider,
    )

    if (
        normalized
        not in SUPPORTED_VISION_PROVIDERS
    ):
        raise InvalidVisionProviderError(
            provider,
        )

    return normalized


def is_supported_vision_provider(
    provider: str,
) -> bool:
    """
    Determine whether a vision provider is supported.
    """
    return (
        normalize_vision_provider(
            provider,
        )
        in SUPPORTED_VISION_PROVIDERS
    )


def validate_vision_id(
    vision_id: str,
) -> str:
    """
    Validate a vision identifier.
    """
    normalized = vision_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            f"Invalid vision identifier: '{vision_id}'."
        )

    return normalized


def build_vision_id() -> str:
    """
    Build a unique vision identifier.
    """
    return f"vision-{uuid.uuid4()}"