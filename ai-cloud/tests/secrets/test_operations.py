"""Tests for ai_cloud.secrets.operations."""

from __future__ import annotations

import pytest

from ai_cloud.secrets.constants import (
    DEFAULT_ENABLED,
    DEFAULT_SECRET_TYPE,
)
from ai_cloud.secrets.exceptions import (
    DuplicateSecretError,
    SecretNotFoundError,
    SecretValidationError,
    UnsupportedSecretTypeError,
)
from ai_cloud.secrets.operations import (
    SecretDefinition,
    SecretRegistry,
    build_secret,
)


def test_secret_definition_defaults() -> None:
    secret = SecretDefinition(
        name="openai",
        value="abc123",
    )

    assert secret.name == "openai"
    assert secret.value == "abc123"
    assert secret.secret_type == DEFAULT_SECRET_TYPE
    assert secret.description == ""
    assert secret.enabled is DEFAULT_ENABLED


def test_secret_definition_trims_values() -> None:
    secret = SecretDefinition(
        name="  openai  ",
        value="  abc123  ",
    )

    assert secret.name == "openai"
    assert secret.value == "abc123"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(
        SecretValidationError,
    ):
        SecretDefinition(
            name=name,
            value="abc123",
        )


@pytest.mark.parametrize(
    "value",
    [
        "",
        "   ",
    ],
)
def test_invalid_value(value: str) -> None:
    with pytest.raises(
        SecretValidationError,
    ):
        SecretDefinition(
            name="openai",
            value=value,
        )


def test_invalid_secret_type() -> None:
    with pytest.raises(
        UnsupportedSecretTypeError,
    ):
        SecretDefinition(
            name="openai",
            value="abc123",
            secret_type="oauth",
        )


def test_build_secret() -> None:
    secret = build_secret(
        name="jwt",
        value="xyz",
        secret_type="token",
        description="JWT token",
    )

    assert secret.name == "jwt"
    assert secret.value == "xyz"
    assert secret.secret_type == "token"
    assert secret.description == "JWT token"


def test_registry_register_and_get() -> None:
    registry = SecretRegistry()

    secret = build_secret(
        name="openai",
        value="abc123",
    )

    registry.register(secret)

    assert registry.get("openai") is secret
    assert registry.exists("openai")
    assert len(registry) == 1
    assert "openai" in registry


def test_registry_duplicate_registration() -> None:
    registry = SecretRegistry()

    secret = build_secret(
        name="openai",
        value="abc123",
    )

    registry.register(secret)

    with pytest.raises(
        DuplicateSecretError,
    ):
        registry.register(secret)


def test_registry_unregister() -> None:
    registry = SecretRegistry()

    secret = build_secret(
        name="openai",
        value="abc123",
    )

    registry.register(secret)
    registry.unregister("openai")

    assert len(registry) == 0
    assert not registry.exists("openai")


def test_registry_unregister_missing() -> None:
    registry = SecretRegistry()

    with pytest.raises(
        SecretNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = SecretRegistry()

    with pytest.raises(
        SecretNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = SecretRegistry()

    registry.register(
        build_secret(
            name="one",
            value="111",
        )
    )
    registry.register(
        build_secret(
            name="two",
            value="222",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = SecretRegistry()

    first = build_secret(
        name="one",
        value="111",
    )
    second = build_secret(
        name="two",
        value="222",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = SecretRegistry()

    assert 123 not in registry