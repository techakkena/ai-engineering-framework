"""
Operations for ai_security.authorization.
"""

from __future__ import annotations

import re
import uuid

from ai_security.authorization.constants import (
    SUPPORTED_AUTHORIZATION_PROVIDERS,
)
from ai_security.authorization.exceptions import (
    InvalidAuthorizationProviderError,
)


def normalize_authorization_provider(
    provider: str,
) -> str:
    """
    Normalize an authorization provider.
    """
    return provider.strip().lower()


def validate_authorization_provider(
    provider: str,
) -> str:
    """
    Validate an authorization provider.
    """
    normalized = (
        normalize_authorization_provider(
            provider,
        )
    )

    if (
        normalized
        not in SUPPORTED_AUTHORIZATION_PROVIDERS
    ):
        raise InvalidAuthorizationProviderError(
            provider,
        )

    return normalized


def is_supported_authorization_provider(
    provider: str,
) -> bool:
    """
    Determine whether an authorization
    provider is supported.
    """
    return (
        normalize_authorization_provider(
            provider,
        )
        in SUPPORTED_AUTHORIZATION_PROVIDERS
    )


def validate_authorization_id(
    authorization_id: str,
) -> str:
    """
    Validate an authorization identifier.
    """
    normalized = (
        authorization_id.strip().lower()
    )

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            (
                "Invalid authorization "
                f"identifier: "
                f"'{authorization_id}'."
            )
        )

    return normalized


def build_authorization_id() -> str:
    """
    Build a unique authorization identifier.
    """
    return (
        f"authorization-{uuid.uuid4()}"
    )