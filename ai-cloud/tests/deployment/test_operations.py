"""Tests for ai_cloud.deployment.operations."""

from __future__ import annotations

import pytest

from ai_cloud.deployment.constants import (
    DEFAULT_DEPLOYMENT_STRATEGY,
    DEFAULT_ENABLED,
)
from ai_cloud.deployment.exceptions import (
    DeploymentNotFoundError,
    DeploymentValidationError,
    DuplicateDeploymentError,
    UnsupportedDeploymentStrategyError,
)
from ai_cloud.deployment.operations import (
    DeploymentDefinition,
    DeploymentRegistry,
    build_deployment,
)


def test_deployment_definition_defaults() -> None:
    deployment = DeploymentDefinition(
        name="production",
        replicas=3,
    )

    assert deployment.name == "production"
    assert deployment.replicas == 3
    assert (
        deployment.strategy
        == DEFAULT_DEPLOYMENT_STRATEGY
    )
    assert deployment.description == ""
    assert deployment.enabled is DEFAULT_ENABLED


def test_deployment_definition_trims_name() -> None:
    deployment = DeploymentDefinition(
        name="  production  ",
        replicas=3,
    )

    assert deployment.name == "production"


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
        DeploymentValidationError,
    ):
        DeploymentDefinition(
            name=name,
            replicas=3,
        )


@pytest.mark.parametrize(
    "replicas",
    [
        0,
        -1,
        -10,
    ],
)
def test_invalid_replicas(
    replicas: int,
) -> None:
    with pytest.raises(
        DeploymentValidationError,
    ):
        DeploymentDefinition(
            name="production",
            replicas=replicas,
        )


def test_invalid_strategy() -> None:
    with pytest.raises(
        UnsupportedDeploymentStrategyError,
    ):
        DeploymentDefinition(
            name="production",
            replicas=3,
            strategy="invalid",
        )


def test_build_deployment() -> None:
    deployment = build_deployment(
        name="production",
        replicas=5,
        strategy="canary",
        description="Canary deployment",
    )

    assert deployment.name == "production"
    assert deployment.replicas == 5
    assert deployment.strategy == "canary"
    assert (
        deployment.description
        == "Canary deployment"
    )


def test_registry_register_and_get() -> None:
    registry = DeploymentRegistry()

    deployment = build_deployment(
        name="production",
        replicas=3,
    )

    registry.register(deployment)

    assert registry.get("production") is deployment
    assert registry.exists("production")
    assert len(registry) == 1
    assert "production" in registry


def test_registry_duplicate_registration() -> None:
    registry = DeploymentRegistry()

    deployment = build_deployment(
        name="production",
        replicas=3,
    )

    registry.register(deployment)

    with pytest.raises(
        DuplicateDeploymentError,
    ):
        registry.register(deployment)


def test_registry_unregister() -> None:
    registry = DeploymentRegistry()

    deployment = build_deployment(
        name="production",
        replicas=3,
    )

    registry.register(deployment)
    registry.unregister("production")

    assert len(registry) == 0
    assert not registry.exists("production")


def test_registry_unregister_missing() -> None:
    registry = DeploymentRegistry()

    with pytest.raises(
        DeploymentNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = DeploymentRegistry()

    with pytest.raises(
        DeploymentNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = DeploymentRegistry()

    registry.register(
        build_deployment(
            name="one",
            replicas=1,
        )
    )
    registry.register(
        build_deployment(
            name="two",
            replicas=2,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = DeploymentRegistry()

    first = build_deployment(
        name="one",
        replicas=1,
    )
    second = build_deployment(
        name="two",
        replicas=2,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = DeploymentRegistry()

    assert 123 not in registry