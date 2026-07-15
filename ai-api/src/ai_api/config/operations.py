"""
Utility operations for the ai_api.config module.

This module provides framework-independent helper functions for
configuration validation, environment handling, and API URL generation.

All functions are deterministic, side-effect free, and easily testable.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

import re

from ai_api.config.constants import (
    DEFAULT_API_PREFIX,
    DEFAULT_API_VERSION,
    DEFAULT_HOST,
    DEFAULT_PORT,
    DEFAULT_SCHEME,
    SUPPORTED_ENVIRONMENTS,
)
from ai_api.config.exceptions import (
    InvalidConfigurationError,
    InvalidEnvironmentError,
)


def normalize_environment(environment: str) -> str:
    """
    Normalize a runtime environment.

    Args:
        environment: Runtime environment.

    Returns:
        Normalized environment.
    """
    return environment.strip().lower()


def validate_environment(environment: str) -> str:
    """
    Validate a runtime environment.

    Args:
        environment: Runtime environment.

    Returns:
        Validated environment.

    Raises:
        InvalidEnvironmentError:
            If the environment is unsupported.
    """
    normalized = normalize_environment(environment)

    if normalized not in SUPPORTED_ENVIRONMENTS:
        raise InvalidEnvironmentError(environment)

    return normalized


def is_supported_environment(environment: str) -> bool:
    """
    Determine whether a runtime environment is supported.

    Args:
        environment: Runtime environment.

    Returns:
        True if supported.
    """
    return (
        normalize_environment(environment)
        in SUPPORTED_ENVIRONMENTS
    )


def validate_configuration_key(key: str) -> str:
    """
    Validate a configuration key.

    Args:
        key: Configuration key.

    Returns:
        Validated configuration key.

    Raises:
        InvalidConfigurationError:
            If the key is invalid.
    """
    normalized = key.strip()

    if not normalized:
        raise InvalidConfigurationError(key, key)

    if not re.fullmatch(
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        normalized,
    ):
        raise InvalidConfigurationError(key, key)

    return normalized


def build_api_url(
    *,
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
    scheme: str = DEFAULT_SCHEME,
    api_prefix: str = DEFAULT_API_PREFIX,
    version: str = DEFAULT_API_VERSION,
) -> str:
    """
    Build an API base URL.

    Args:
        host: Host name.
        port: TCP port.
        scheme: URL scheme.
        api_prefix: API prefix.
        version: API version.

    Returns:
        Fully qualified API URL.
    """
    prefix = api_prefix.strip("/")

    return (
        f"{scheme}://{host}:{port}/"
        f"{prefix}/{version}"
    )


def validate_port(port: int) -> int:
    """
    Validate a TCP port number.

    Args:
        port: TCP port.

    Returns:
        Validated port.

    Raises:
        InvalidConfigurationError:
            If the port is invalid.
    """
    if not (1 <= port <= 65535):
        raise InvalidConfigurationError(
            "port",
            port,
        )

    return port


def validate_host(host: str) -> str:
    """
    Validate a host name.

    Args:
        host: Host name.

    Returns:
        Validated host.

    Raises:
        InvalidConfigurationError:
            If the host is invalid.
    """
    normalized = host.strip()

    if not normalized:
        raise InvalidConfigurationError(
            "host",
            host,
        )

    return normalized


def normalize_api_prefix(
    api_prefix: str,
) -> str:
    """
    Normalize an API prefix.

    Args:
        api_prefix: API prefix.

    Returns:
        Normalized API prefix.
    """
    normalized = api_prefix.strip()

    if not normalized.startswith("/"):
        normalized = "/" + normalized

    return normalized.rstrip("/")