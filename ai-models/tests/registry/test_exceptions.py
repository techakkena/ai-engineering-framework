"""
Unit tests for ai_models.registry.exceptions.
"""

from __future__ import annotations

import pytest

from ai_models.registry.exceptions import (
    InvalidRegistryProviderError,
    RegistryConfigurationError,
    RegistryError,
    RegistryValidationError,
)


def test_registry_error_default_message() -> None:
    """Test RegistryError default message."""
    error = RegistryError()

    assert (
        str(error)
        == "A registry error occurred."
    )


def test_registry_error_custom_message() -> None:
    """Test RegistryError custom message."""
    error = RegistryError(
        "Custom registry error.",
    )

    assert (
        str(error)
        == "Custom registry error."
    )


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "bedrock",
        "vertex",
    ],
)
def test_invalid_registry_provider_error(
    provider: str,
) -> None:
    """Test InvalidRegistryProviderError."""
    error = InvalidRegistryProviderError(
        provider,
    )

    assert isinstance(
        error,
        RegistryError,
    )

    assert error.provider == provider

    assert (
        str(error)
        == (
            "Invalid registry provider: "
            f"'{provider}'."
        )
    )


def test_registry_configuration_error() -> None:
    """Test RegistryConfigurationError."""
    configuration = "cache_size"

    error = RegistryConfigurationError(
        configuration,
    )

    assert isinstance(
        error,
        RegistryError,
    )

    assert (
        error.configuration
        == configuration
    )

    assert (
        str(error)
        == (
            "Invalid registry "
            "configuration: "
            f"'{configuration}'."
        )
    )


def test_registry_validation_error() -> None:
    """Test RegistryValidationError."""
    registry = "default"
    reason = "duplicate model"

    error = RegistryValidationError(
        registry,
        reason,
    )

    assert isinstance(
        error,
        RegistryError,
    )

    assert error.registry == registry
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Registry '{registry}' "
            f"validation failed: "
            f"{reason}."
        )
    )