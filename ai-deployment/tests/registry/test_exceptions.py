"""
Tests for ai_deployment.registry.exceptions.
"""

from ai_deployment.registry.exceptions import (
    RegistryConfigurationError,
    RegistryError,
    RegistryOperationError,
)


def test_registry_error() -> None:
    error = RegistryError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    assert isinstance(
        RegistryConfigurationError("config"),
        RegistryError,
    )


def test_operation_error() -> None:
    assert isinstance(
        RegistryOperationError("operation"),
        RegistryError,
    )