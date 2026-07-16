"""Tests for ai_cloud.providers.operations."""

from __future__ import annotations

import pytest

from ai_cloud.providers.constants import (
    DEFAULT_ENABLED,
    DEFAULT_PROVIDER_TYPE,
)
from ai_cloud.providers.exceptions import (
    DuplicateProviderError,
    ProviderNotFoundError,
    ProviderValidationError,
    UnsupportedProviderTypeError,
)
from ai_cloud.providers.operations import (
    CloudProvider,
    CloudProviderRegistry,
    build_provider,
)


def test_provider_defaults() -> None:
    provider = CloudProvider(
        name="production",
        region="us-east-1",
    )

    assert provider.name == "production"
    assert provider.region == "us-east-1"
    assert provider.provider_type == DEFAULT_PROVIDER_TYPE
    assert provider.description == ""
    assert provider.enabled is DEFAULT_ENABLED


def test_provider_trims_values() -> None:
    provider = CloudProvider(
        name="  production  ",
        region=" us-east-1 ",
    )

    assert provider.name == "production"
    assert provider.region == "us-east-1"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_provider_name(
    name: str,
) -> None:
    with pytest.raises(
        ProviderValidationError,
    ):
        CloudProvider(
            name=name,
            region="us-east-1",
        )


@pytest.mark.parametrize(
    "region",
    [
        "",
        "   ",
    ],
)
def test_invalid_region(
    region: str,
) -> None:
    with pytest.raises(
        ProviderValidationError,
    ):
        CloudProvider(
            name="production",
            region=region,
        )


def test_invalid_provider_type() -> None:
    with pytest.raises(
        UnsupportedProviderTypeError,
    ):
        CloudProvider(
            name="production",
            region="us-east-1",
            provider_type="digitalocean",
        )


def test_build_provider() -> None:
    provider = build_provider(
        name="azure-prod",
        region="eastus",
        provider_type="azure",
        description="Azure production",
    )

    assert provider.name == "azure-prod"
    assert provider.region == "eastus"
    assert provider.provider_type == "azure"
    assert provider.description == "Azure production"


def test_registry_register_and_get() -> None:
    registry = CloudProviderRegistry()

    provider = build_provider(
        name="aws-prod",
        region="us-east-1",
    )

    registry.register(provider)

    assert registry.get("aws-prod") is provider
    assert registry.exists("aws-prod")
    assert len(registry) == 1
    assert "aws-prod" in registry


def test_registry_duplicate_registration() -> None:
    registry = CloudProviderRegistry()

    provider = build_provider(
        name="aws-prod",
        region="us-east-1",
    )

    registry.register(provider)

    with pytest.raises(
        DuplicateProviderError,
    ):
        registry.register(provider)


def test_registry_unregister() -> None:
    registry = CloudProviderRegistry()

    provider = build_provider(
        name="aws-prod",
        region="us-east-1",
    )

    registry.register(provider)
    registry.unregister("aws-prod")

    assert len(registry) == 0
    assert not registry.exists("aws-prod")


def test_registry_unregister_missing() -> None:
    registry = CloudProviderRegistry()

    with pytest.raises(
        ProviderNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = CloudProviderRegistry()

    with pytest.raises(
        ProviderNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = CloudProviderRegistry()

    registry.register(
        build_provider(
            name="one",
            region="us-east-1",
        )
    )
    registry.register(
        build_provider(
            name="two",
            region="eu-west-1",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = CloudProviderRegistry()

    first = build_provider(
        name="one",
        region="us-east-1",
    )
    second = build_provider(
        name="two",
        region="eu-west-1",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = CloudProviderRegistry()

    assert 123 not in registry