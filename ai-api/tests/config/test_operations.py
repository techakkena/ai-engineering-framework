"""
Unit tests for ai_api.config.operations.
"""

from __future__ import annotations

import pytest

from ai_api.config.exceptions import (
    InvalidConfigurationError,
    InvalidEnvironmentError,
)
from ai_api.config.operations import (
    build_api_url,
    is_supported_environment,
    normalize_api_prefix,
    normalize_environment,
    validate_configuration_key,
    validate_environment,
    validate_host,
    validate_port,
)


# ============================================================================
# normalize_environment
# ============================================================================


@pytest.mark.parametrize(
    ("environment", "expected"),
    [
        ("Development", "development"),
        (" TESTING ", "testing"),
        ("Production", "production"),
        ("Staging", "staging"),
    ],
)
def test_normalize_environment(
    environment: str,
    expected: str,
) -> None:
    """Test environment normalization."""
    assert normalize_environment(environment) == expected


# ============================================================================
# validate_environment
# ============================================================================


@pytest.mark.parametrize(
    "environment",
    [
        "development",
        "testing",
        "staging",
        "production",
    ],
)
def test_validate_environment(
    environment: str,
) -> None:
    """Test supported environments."""
    assert validate_environment(environment) == environment


@pytest.mark.parametrize(
    "environment",
    [
        "",
        "local",
        "sandbox",
        "uat",
    ],
)
def test_validate_environment_invalid(
    environment: str,
) -> None:
    """Unsupported environments should raise."""
    with pytest.raises(
        InvalidEnvironmentError,
    ):
        validate_environment(environment)


# ============================================================================
# is_supported_environment
# ============================================================================


@pytest.mark.parametrize(
    ("environment", "expected"),
    [
        ("development", True),
        ("testing", True),
        ("staging", True),
        ("production", True),
        ("local", False),
        ("sandbox", False),
    ],
)
def test_is_supported_environment(
    environment: str,
    expected: bool,
) -> None:
    """Test supported environment detection."""
    assert (
        is_supported_environment(environment)
        is expected
    )


# ============================================================================
# validate_configuration_key
# ============================================================================


@pytest.mark.parametrize(
    "key",
    [
        "host",
        "port",
        "database_url",
        "api_key",
        "timeout",
    ],
)
def test_validate_configuration_key(
    key: str,
) -> None:
    """Test valid configuration keys."""
    assert validate_configuration_key(key) == key


@pytest.mark.parametrize(
    "key",
    [
        "",
        "123key",
        "invalid-key",
        "invalid key",
        "@config",
    ],
)
def test_validate_configuration_key_invalid(
    key: str,
) -> None:
    """Invalid configuration keys should raise."""
    with pytest.raises(
        InvalidConfigurationError,
    ):
        validate_configuration_key(key)


# ============================================================================
# build_api_url
# ============================================================================


def test_build_api_url_default() -> None:
    """Test default API URL generation."""
    assert (
        build_api_url()
        == "http://127.0.0.1:8000/api/v1"
    )


def test_build_api_url_custom() -> None:
    """Test custom API URL generation."""
    assert (
        build_api_url(
            host="example.com",
            port=443,
            scheme="https",
            api_prefix="/service",
            version="v2",
        )
        == "https://example.com:443/service/v2"
    )


# ============================================================================
# validate_port
# ============================================================================


@pytest.mark.parametrize(
    "port",
    [
        1,
        80,
        443,
        8000,
        65535,
    ],
)
def test_validate_port(
    port: int,
) -> None:
    """Test valid TCP ports."""
    assert validate_port(port) == port


@pytest.mark.parametrize(
    "port",
    [
        0,
        -1,
        65536,
        100000,
    ],
)
def test_validate_port_invalid(
    port: int,
) -> None:
    """Invalid ports should raise."""
    with pytest.raises(
        InvalidConfigurationError,
    ):
        validate_port(port)


# ============================================================================
# validate_host
# ============================================================================


@pytest.mark.parametrize(
    "host",
    [
        "localhost",
        "127.0.0.1",
        "example.com",
    ],
)
def test_validate_host(
    host: str,
) -> None:
    """Test valid hosts."""
    assert validate_host(host) == host


@pytest.mark.parametrize(
    "host",
    [
        "",
        " ",
    ],
)
def test_validate_host_invalid(
    host: str,
) -> None:
    """Invalid hosts should raise."""
    with pytest.raises(
        InvalidConfigurationError,
    ):
        validate_host(host)


# ============================================================================
# normalize_api_prefix
# ============================================================================


@pytest.mark.parametrize(
    ("prefix", "expected"),
    [
        ("api", "/api"),
        ("/api", "/api"),
        ("api/", "/api"),
        ("/api/", "/api"),
        ("service/v1", "/service/v1"),
    ],
)
def test_normalize_api_prefix(
    prefix: str,
    expected: str,
) -> None:
    """Test API prefix normalization."""
    assert normalize_api_prefix(prefix) == expected