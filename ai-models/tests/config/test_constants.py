"""
Operations for ai_models.config.
"""

from __future__ import annotations

import re
import uuid

from ai_models.config.constants import (
    SUPPORTED_ENVIRONMENTS,
)
from ai_models.config.exceptions import (
    InvalidEnvironmentError,
)


def normalize_environment(
    environment: str,
) -> str:
    """
    Normalize an environment name.

    Args:
        environment:
            Environment name.

    Returns:
        Normalized environment.
    """
    return environment.strip().lower()


def validate_environment(
    environment: str,
) -> str:
    """
    Validate an environment.

    Args:
        environment:
            Environment name.

    Returns:
        Normalized environment.

    Raises:
        InvalidEnvironmentError:
            If the environment is unsupported.
    """
    normalized = normalize_environment(
        environment,
    )

    if (
        normalized
        not in SUPPORTED_ENVIRONMENTS
    ):
        raise InvalidEnvironmentError(
            environment,
        )

    return normalized


def is_supported_environment(
    environment: str,
) -> bool:
    """
    Determine whether an environment is supported.

    Args:
        environment:
            Environment name.

    Returns:
        True if supported.
    """
    return (
        normalize_environment(
            environment,
        )
        in SUPPORTED_ENVIRONMENTS
    )


def validate_configuration_id(
    configuration_id: str,
) -> str:
    """
    Validate a configuration identifier.

    Args:
        configuration_id:
            Configuration identifier.

    Returns:
        Normalized identifier.

    Raises:
        ValueError:
            If the identifier is invalid.
    """
    normalized = (
        configuration_id.strip().lower()
    )

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            (
                "Invalid configuration "
                f"identifier: "
                f"'{configuration_id}'."
            )
        )

    return normalized


def build_configuration_id() -> str:
    """
    Build a unique configuration identifier.

    Returns:
        A unique configuration identifier.
    """
    return (
        f"config-{uuid.uuid4()}"
    )