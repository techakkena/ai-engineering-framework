"""Tests for ai_testing.mocks.operations."""

from __future__ import annotations

import pytest

from ai_testing.mocks.constants import (
    DEFAULT_ENABLED,
    DEFAULT_RESET_AFTER_USE,
)
from ai_testing.mocks.exceptions import (
    DuplicateMockError,
    MockNotFoundError,
    MockValidationError,
)
from ai_testing.mocks.operations import (
    MockDefinition,
    MockRegistry,
    build_mock,
)


def test_mock_definition_defaults() -> None:
    mock = MockDefinition(
        name="service",
        target="package.service",
        value=1,
    )

    assert mock.name == "service"
    assert mock.target == "package.service"
    assert mock.value == 1
    assert mock.enabled is DEFAULT_ENABLED
    assert mock.reset_after_use is DEFAULT_RESET_AFTER_USE


def test_mock_definition_trims_values() -> None:
    mock = MockDefinition(
        name="  service  ",
        target="  package.service  ",
        value=1,
    )

    assert mock.name == "service"
    assert mock.target == "package.service"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(MockValidationError):
        MockDefinition(
            name=name,
            target="package.service",
            value=1,
        )


@pytest.mark.parametrize(
    "target",
    [
        "",
        "   ",
    ],
)
def test_invalid_target(target: str) -> None:
    with pytest.raises(MockValidationError):
        MockDefinition(
            name="service",
            target=target,
            value=1,
        )


def test_build_mock() -> None:
    mock = build_mock(
        name="database",
        target="database.connect",
        value={"host": "localhost"},
    )

    assert mock.name == "database"
    assert mock.target == "database.connect"
    assert mock.value == {"host": "localhost"}


def test_registry_register_get() -> None:
    registry = MockRegistry()

    mock = build_mock(
        name="service",
        target="service.call",
        value=1,
    )

    registry.register(mock)

    assert registry.get("service") is mock
    assert registry.exists("service")
    assert len(registry) == 1
    assert "service" in registry


def test_registry_duplicate_registration() -> None:
    registry = MockRegistry()

    mock = build_mock(
        name="service",
        target="service.call",
        value=1,
    )

    registry.register(mock)

    with pytest.raises(DuplicateMockError):
        registry.register(mock)


def test_registry_unregister() -> None:
    registry = MockRegistry()

    mock = build_mock(
        name="service",
        target="service.call",
        value=1,
    )

    registry.register(mock)
    registry.unregister("service")

    assert len(registry) == 0
    assert not registry.exists("service")


def test_registry_unregister_missing() -> None:
    registry = MockRegistry()

    with pytest.raises(MockNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = MockRegistry()

    with pytest.raises(MockNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = MockRegistry()

    registry.register(
        build_mock(
            name="one",
            target="target.one",
            value=1,
        )
    )
    registry.register(
        build_mock(
            name="two",
            target="target.two",
            value=2,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = MockRegistry()

    first = build_mock(
        name="one",
        target="target.one",
        value=1,
    )
    second = build_mock(
        name="two",
        target="target.two",
        value=2,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = MockRegistry()

    assert 123 not in registry