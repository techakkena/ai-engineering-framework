"""Tests for ai_cloud.authentication.operations."""

from __future__ import annotations

import pytest

from ai_cloud.authentication.constants import (
    DEFAULT_AUTHENTICATION_TYPE,
    DEFAULT_ENABLED,
)
from ai_cloud.authentication.exceptions import (
    AuthenticationNotFoundError,
    AuthenticationValidationError,
    DuplicateAuthenticationError,
    UnsupportedAuthenticationTypeError,
)
from ai_cloud.authentication.operations import (
    AuthenticationDefinition,
    AuthenticationRegistry,
    build_authentication,
)


def test_authentication_definition_defaults() -> None:
    authentication = AuthenticationDefinition(
        name="service-account",
        credential="secret",
    )

    assert authentication.name == "service-account"
    assert authentication.credential == "secret"
    assert (
        authentication.authentication_type
        == DEFAULT_AUTHENTICATION_TYPE
    )
    assert authentication.description == ""
    assert authentication.enabled is DEFAULT_ENABLED


def test_authentication_definition_trims_values() -> None:
    authentication = AuthenticationDefinition(
        name="  service-account  ",
        credential="  token123  ",
    )

    assert authentication.name == "service-account"
    assert authentication.credential == "token123"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(
    name: str,
) -> None:
    with pytest.raises(
        AuthenticationValidationError,
    ):
        AuthenticationDefinition(
            name=name,
            credential="secret",
        )


@pytest.mark.parametrize(
    "credential",
    [
        "",
        "   ",
    ],
)
def test_invalid_credential(
    credential: str,
) -> None:
    with pytest.raises(
        AuthenticationValidationError,
    ):
        AuthenticationDefinition(
            name="service-account",
            credential=credential,
        )


def test_invalid_authentication_type() -> None:
    with pytest.raises(
        UnsupportedAuthenticationTypeError,
    ):
        AuthenticationDefinition(
            name="service-account",
            credential="secret",
            authentication_type="ldap",
        )


def test_build_authentication() -> None:
    authentication = build_authentication(
        name="jwt-auth",
        credential="token",
        authentication_type="jwt",
        description="JWT authentication",
    )

    assert authentication.name == "jwt-auth"
    assert authentication.credential == "token"
    assert authentication.authentication_type == "jwt"
    assert (
        authentication.description
        == "JWT authentication"
    )


def test_registry_register_and_get() -> None:
    registry = AuthenticationRegistry()

    authentication = build_authentication(
        name="service-account",
        credential="secret",
    )

    registry.register(authentication)

    assert (
        registry.get("service-account")
        is authentication
    )
    assert registry.exists("service-account")
    assert len(registry) == 1
    assert "service-account" in registry


def test_registry_duplicate_registration() -> None:
    registry = AuthenticationRegistry()

    authentication = build_authentication(
        name="service-account",
        credential="secret",
    )

    registry.register(authentication)

    with pytest.raises(
        DuplicateAuthenticationError,
    ):
        registry.register(authentication)


def test_registry_unregister() -> None:
    registry = AuthenticationRegistry()

    authentication = build_authentication(
        name="service-account",
        credential="secret",
    )

    registry.register(authentication)
    registry.unregister("service-account")

    assert len(registry) == 0
    assert not registry.exists("service-account")


def test_registry_unregister_missing() -> None:
    registry = AuthenticationRegistry()

    with pytest.raises(
        AuthenticationNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = AuthenticationRegistry()

    with pytest.raises(
        AuthenticationNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = AuthenticationRegistry()

    registry.register(
        build_authentication(
            name="one",
            credential="one",
        )
    )
    registry.register(
        build_authentication(
            name="two",
            credential="two",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = AuthenticationRegistry()

    first = build_authentication(
        name="one",
        credential="one",
    )
    second = build_authentication(
        name="two",
        credential="two",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = AuthenticationRegistry()

    assert 123 not in registry