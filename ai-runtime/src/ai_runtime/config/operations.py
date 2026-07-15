"""
Operations for ai_runtime.config.
"""

from __future__ import annotations

import re
import uuid

from ai_runtime.config.constants import (
    SUPPORTED_ENVIRONMENTS,
)
from ai_runtime.config.exceptions import (
    InvalidEnvironmentError,
)


def normalize_environment(
    environment: str,
) -> str:
    """
    Normalize an environment name.
    """
    return environment.strip().lower()


def validate_environment(
    environment: str,
) -> str:
    """
    Validate an environment.
    """
    normalized = normalize_environment(environment)

    if normalized not in SUPPORTED_ENVIRONMENTS:
        raise InvalidEnvironmentError(environment)

    return normalized


def is_supported_environment(
    environment: str,
) -> bool:
    """
    Determine whether an environment is supported.
    """
    return (
        normalize_environment(environment)
        in SUPPORTED_ENVIRONMENTS
    )


def validate_config_id(
    config_id: str,
) -> str:
    """
    Validate a configuration identifier.
    """
    normalized = config_id.strip().lower()

    if not re.fullmatch(
        r"[a-z][a-z0-9_-]*",
        normalized,
    ):
        raise ValueError(
            f"Invalid configuration identifier: '{config_id}'."
        )

    return normalized


def build_config_id() -> str:
    """
    Build a unique configuration identifier.

    Returns:
        Configuration identifier.
    """
    return f"config-{uuid.uuid4()}"