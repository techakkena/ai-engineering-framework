"""
Unit tests for ai_models.config.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_models.config.exceptions import (
    InvalidEnvironmentError,
)
from ai_models.config.operations import (
    build_configuration_id,
    is_supported_environment,
    normalize_environment,
    validate_configuration_id,
    validate_environment,
)


# ============================================================================
# normalize_environment
# ============================================================================


@pytest.mark.parametrize(
    ("environment", "expected"),
    [
        ("DEVELOPMENT", "development"),
        (" Testing ", "testing"),
        ("Staging", "staging"),
        ("PRODUCTION", "production"),
    ],
)
def test_normalize_environment(
    environment: str,
    expected: str,
) -> None:
    """Test environment normalization."""
    assert (
        normalize_environment(
            environment,
        )
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
    """Test valid environments."""
    assert (
        validate_environment(
            environment,
        )
        == environment
    )


@pytest.mark.parametrize(
    "environment",
    [
        "",
        "local",
        "uat",
        "qa",
    ],
)
def test_validate_environment_invalid(
    environment: str,
) -> None:
    """Invalid environments should raise."""
    with pytest.raises(
        InvalidEnvironmentError,
    ):
        validate_environment(
            environment,
        )


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
        ("uat", False),
    ],
)
def test_is_supported_environment(
    environment: str,
    expected: bool,
) -> None:
    """Test environment support detection."""
    assert (
        is_supported_environment(
            environment,
        )
        is expected
    )


# ============================================================================
# validate_configuration_id
# ============================================================================


@pytest.mark.parametrize(
    "configuration_id",
    [
        "config",
        "config_01",
        "config-01",
        "runtime123",
    ],
)
def test_validate_configuration_id(
    configuration_id: str,
) -> None:
    """Test valid configuration identifiers."""
    assert (
        validate_configuration_id(
            configuration_id,
        )
        == configuration_id.lower()
    )


@pytest.mark.parametrize(
    "configuration_id",
    [
        "",
        "123config",
        "config name",
        "@config",
    ],
)
def test_validate_configuration_id_invalid(
    configuration_id: str,
) -> None:
    """Invalid identifiers should raise."""
    with pytest.raises(ValueError):
        validate_configuration_id(
            configuration_id,
        )


# ============================================================================
# build_configuration_id
# ============================================================================


def test_build_configuration_id() -> None:
    """Test configuration ID generation."""
    configuration_id = (
        build_configuration_id()
    )

    assert configuration_id.startswith(
        "config-",
    )

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
        pattern.fullmatch(
            configuration_id,
        )
        is not None
    )