"""Tests for ai_cloud.networking.operations."""

from __future__ import annotations

import pytest

from ai_cloud.networking.constants import (
    DEFAULT_ENABLED,
    DEFAULT_NETWORK_TYPE,
)
from ai_cloud.networking.exceptions import (
    DuplicateNetworkError,
    NetworkNotFoundError,
    NetworkValidationError,
    UnsupportedNetworkTypeError,
)
from ai_cloud.networking.operations import (
    NetworkDefinition,
    NetworkRegistry,
    build_network,
)


def test_network_definition_defaults() -> None:
    network = NetworkDefinition(
        name="production",
        cidr="10.0.0.0/16",
    )

    assert network.name == "production"
    assert network.cidr == "10.0.0.0/16"
    assert network.network_type == DEFAULT_NETWORK_TYPE
    assert network.description == ""
    assert network.enabled is DEFAULT_ENABLED


def test_network_definition_trims_values() -> None:
    network = NetworkDefinition(
        name="  production  ",
        cidr=" 10.0.0.0/16 ",
    )

    assert network.name == "production"
    assert network.cidr == "10.0.0.0/16"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(NetworkValidationError):
        NetworkDefinition(
            name=name,
            cidr="10.0.0.0/16",
        )


@pytest.mark.parametrize(
    "cidr",
    [
        "",
        "   ",
    ],
)
def test_invalid_cidr(cidr: str) -> None:
    with pytest.raises(NetworkValidationError):
        NetworkDefinition(
            name="production",
            cidr=cidr,
        )


def test_invalid_network_type() -> None:
    with pytest.raises(
        UnsupportedNetworkTypeError,
    ):
        NetworkDefinition(
            name="production",
            cidr="10.0.0.0/16",
            network_type="mesh",
        )


def test_build_network() -> None:
    network = build_network(
        name="public-net",
        cidr="192.168.1.0/24",
        network_type="public",
        description="Public network",
    )

    assert network.name == "public-net"
    assert network.cidr == "192.168.1.0/24"
    assert network.network_type == "public"
    assert network.description == "Public network"


def test_registry_register_and_get() -> None:
    registry = NetworkRegistry()

    network = build_network(
        name="production",
        cidr="10.0.0.0/16",
    )

    registry.register(network)

    assert registry.get("production") is network
    assert registry.exists("production")
    assert len(registry) == 1
    assert "production" in registry


def test_registry_duplicate_registration() -> None:
    registry = NetworkRegistry()

    network = build_network(
        name="production",
        cidr="10.0.0.0/16",
    )

    registry.register(network)

    with pytest.raises(
        DuplicateNetworkError,
    ):
        registry.register(network)


def test_registry_unregister() -> None:
    registry = NetworkRegistry()

    network = build_network(
        name="production",
        cidr="10.0.0.0/16",
    )

    registry.register(network)
    registry.unregister("production")

    assert len(registry) == 0
    assert not registry.exists("production")


def test_registry_unregister_missing() -> None:
    registry = NetworkRegistry()

    with pytest.raises(
        NetworkNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = NetworkRegistry()

    with pytest.raises(
        NetworkNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = NetworkRegistry()

    registry.register(
        build_network(
            name="one",
            cidr="10.0.0.0/24",
        )
    )
    registry.register(
        build_network(
            name="two",
            cidr="10.0.1.0/24",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = NetworkRegistry()

    first = build_network(
        name="one",
        cidr="10.0.0.0/24",
    )
    second = build_network(
        name="two",
        cidr="10.0.1.0/24",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = NetworkRegistry()

    assert 123 not in registry