"""Tests for ai_testing.fixtures.operations."""

from __future__ import annotations

import pytest

from ai_testing.fixtures.constants import DEFAULT_FIXTURE_SCOPE
from ai_testing.fixtures.exceptions import (
    DuplicateFixtureError,
    FixtureNotFoundError,
    FixtureValidationError,
    UnsupportedFixtureScopeError,
)
from ai_testing.fixtures.operations import (
    FixtureDefinition,
    FixtureRegistry,
    build_fixture,
)


def test_fixture_definition_defaults() -> None:
    fixture = FixtureDefinition(
        name="sample",
        value=123,
    )

    assert fixture.name == "sample"
    assert fixture.value == 123
    assert fixture.scope == DEFAULT_FIXTURE_SCOPE
    assert fixture.autouse is False
    assert fixture.cache is True
    assert fixture.description == ""
    assert fixture.tags == ()


def test_fixture_name_trimmed() -> None:
    fixture = FixtureDefinition(
        name="  sample  ",
        value=1,
    )

    assert fixture.name == "sample"


@pytest.mark.parametrize(
    "name",
    [
        "",
        " " * 5,
        "a" * 256,
    ],
)
def test_fixture_invalid_name(name: str) -> None:
    with pytest.raises(FixtureValidationError):
        FixtureDefinition(
            name=name,
            value=None,
        )


def test_fixture_invalid_scope() -> None:
    with pytest.raises(UnsupportedFixtureScopeError):
        FixtureDefinition(
            name="fixture",
            value=1,
            scope="invalid",
        )


def test_build_fixture() -> None:
    fixture = build_fixture(
        name="database",
        value={"url": "sqlite://"},
    )

    assert fixture.name == "database"
    assert fixture.value == {"url": "sqlite://"}


def test_registry_register_and_get() -> None:
    registry = FixtureRegistry()

    fixture = build_fixture(
        name="sample",
        value=1,
    )

    registry.register(fixture)

    assert registry.get("sample") is fixture
    assert registry.exists("sample")
    assert len(registry) == 1
    assert "sample" in registry


def test_registry_duplicate_registration() -> None:
    registry = FixtureRegistry()

    fixture = build_fixture(
        name="sample",
        value=1,
    )

    registry.register(fixture)

    with pytest.raises(DuplicateFixtureError):
        registry.register(fixture)


def test_registry_unregister() -> None:
    registry = FixtureRegistry()

    fixture = build_fixture(
        name="sample",
        value=1,
    )

    registry.register(fixture)
    registry.unregister("sample")

    assert len(registry) == 0
    assert not registry.exists("sample")


def test_registry_unregister_missing() -> None:
    registry = FixtureRegistry()

    with pytest.raises(FixtureNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = FixtureRegistry()

    with pytest.raises(FixtureNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = FixtureRegistry()

    registry.register(build_fixture(name="one", value=1))
    registry.register(build_fixture(name="two", value=2))

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = FixtureRegistry()

    first = build_fixture(name="one", value=1)
    second = build_fixture(name="two", value=2)

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = FixtureRegistry()

    assert 123 not in registry