"""Tests for ai_enterprise.users.operations."""

from __future__ import annotations

import pytest

from ai_enterprise.users.constants import (
    DEFAULT_ENABLED,
    DEFAULT_USER_ROLE,
)
from ai_enterprise.users.exceptions import (
    DuplicateUserError,
    UnsupportedUserRoleError,
    UserNotFoundError,
    UserValidationError,
)
from ai_enterprise.users.operations import (
    EnterpriseUser,
    UserRegistry,
    build_user,
)


def test_user_defaults() -> None:
    user = EnterpriseUser(
        username="john",
        email="john@example.com",
    )

    assert user.username == "john"
    assert user.email == "john@example.com"
    assert user.role == DEFAULT_USER_ROLE
    assert user.enabled is DEFAULT_ENABLED


def test_user_trims_values() -> None:
    user = EnterpriseUser(
        username="  john  ",
        email="  john@example.com  ",
    )

    assert user.username == "john"
    assert user.email == "john@example.com"


@pytest.mark.parametrize(
    "username",
    [
        "",
        "  ",
        "ab",
        "a" * 256,
    ],
)
def test_invalid_username(
    username: str,
) -> None:
    with pytest.raises(
        UserValidationError,
    ):
        EnterpriseUser(
            username=username,
            email="john@example.com",
        )


@pytest.mark.parametrize(
    "email",
    [
        "",
        "abc",
        "example.com",
        "@",
    ],
)
def test_invalid_email(
    email: str,
) -> None:
    with pytest.raises(
        UserValidationError,
    ):
        EnterpriseUser(
            username="john",
            email=email,
        )


def test_invalid_role() -> None:
    with pytest.raises(
        UnsupportedUserRoleError,
    ):
        EnterpriseUser(
            username="john",
            email="john@example.com",
            role="developer",
        )


def test_build_user() -> None:
    user = build_user(
        username="admin",
        email="admin@example.com",
        role="admin",
    )

    assert user.username == "admin"
    assert user.email == "admin@example.com"
    assert user.role == "admin"


def test_registry_register_and_get() -> None:
    registry = UserRegistry()

    user = build_user(
        username="john",
        email="john@example.com",
    )

    registry.register(user)

    assert registry.get("john") is user
    assert registry.exists("john")
    assert len(registry) == 1
    assert "john" in registry


def test_registry_duplicate_registration() -> None:
    registry = UserRegistry()

    user = build_user(
        username="john",
        email="john@example.com",
    )

    registry.register(user)

    with pytest.raises(
        DuplicateUserError,
    ):
        registry.register(user)


def test_registry_unregister() -> None:
    registry = UserRegistry()

    user = build_user(
        username="john",
        email="john@example.com",
    )

    registry.register(user)
    registry.unregister("john")

    assert len(registry) == 0
    assert not registry.exists("john")


def test_registry_unregister_missing() -> None:
    registry = UserRegistry()

    with pytest.raises(
        UserNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = UserRegistry()

    with pytest.raises(
        UserNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = UserRegistry()

    registry.register(
        build_user(
            username="one",
            email="one@test.com",
        )
    )
    registry.register(
        build_user(
            username="two",
            email="two@test.com",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = UserRegistry()

    first = build_user(
        username="one",
        email="one@test.com",
    )
    second = build_user(
        username="two",
        email="two@test.com",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = UserRegistry()

    assert 123 not in registry