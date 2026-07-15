"""
Operations for ai_security.authentication.
"""

from __future__ import annotations

import re
import uuid

from ai_security.authentication.constants import (
    SUPPORTED_AUTH_PROVIDERS,
)
from ai_security.authentication.exceptions import (
    InvalidAuthenticationProviderError,
)


def normalize_authentication_provider(
    provider: str,
) -> str:
    """
    Normalize an authentication provider.
    """
    return provider.strip().lower()


def validate_authentication_provider(
    provider: str,
) -> str:
    """
    Validate an authentication provider.
    """
    normalized = (
        normalize_authentication_provider(
            provider,
        )
    )

    if (
        normalized
        not in SUPPORTED_AUTH_PROVIDERS
    ):
        raise InvalidAuthenticationProviderError(
            provider,
        )

    return normalized


def is_supported_authentication_provider(
    provider: str,
) -> bool:
    """
    Determine whether a provider is supported.
    """
    return (
        normalize_authentication_provider(
            provider,
        )
        in SUPPORTED_AUTH_PROVIDERS
    )


def validate_authentication_id(
    authentication_id: str,
) -> str:
    """
    Validate an authentication identifier.
    """
    normalized = (
        authentication_id.strip().lower()
    )

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            (
                "Invalid authentication "
                f"identifier: "
                f"'{authentication_id}'."
            )
        )

    return normalized


def build_authentication_id() -> str:
    """
    Build a unique authentication identifier.
    """
    return (
        f"auth-{uuid.uuid4()}"
    )