"""
Unit tests for ai_runtime.config.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_runtime.config.exceptions import (
    InvalidEnvironmentError,
)
from ai_runtime.config.operations import (
    build_config_id,
    is_supported_environment,
    normalize_environment,
    validate_config_id,
    validate_environment,
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
    assert (
        normalize_environment(environment)
        == expected
    )


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
    assert (
        validate_environment(environment)
        == environment
    )


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
    """Invalid environments should raise."""
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
# validate_config_id
# ============================================================================


@pytest.mark.parametrize(
    "config_id",
    [
        "config",
        "config_01",
        "config-01",
        "runtime123",
    ],
)
def test_validate_config_id(
    config_id: str,
) -> None:
    """Test valid configuration identifiers."""
    assert (
        validate_config_id(config_id)
        == config_id.lower()
    )


@pytest.mark.parametrize(
    "config_id",
    [
        "",
        "123config",
        "config name",
        "@config",
    ],
)
def test_validate_config_id_invalid(
    config_id: str,
) -> None:
    """Invalid configuration identifiers should raise."""
    with pytest.raises(ValueError):
        validate_config_id(config_id)


# ============================================================================
# build_config_id
# ============================================================================


def test_build_config_id() -> None:
    """Test configuration ID generation."""
    config_id = build_config_id()

    assert config_id.startswith("config-")

    pattern = re.compile(
        (
            r"^config-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert (
        pattern.fullmatch(config_id)
        is not None
    )