"""
Tests for ai_deployment.registry.operations.
"""

import pytest

from ai_deployment.registry.exceptions import (
    RegistryConfigurationError,
    RegistryOperationError,
)
from ai_deployment.registry.operations import (
    RegistryArtifact,
    RegistryService,
)


def test_artifact_uri() -> None:
    artifact = RegistryArtifact(
        name="ai-api",
        tag="1.0.0",
    )

    assert (
        artifact.uri
        == "docker.io/library/ai-api:1.0.0"
    )


def test_publish() -> None:
    service = RegistryService()

    artifact = RegistryArtifact(
        name="ai-api",
        tag="1.0.0",
    )

    assert service.publish(artifact)


def test_pull() -> None:
    service = RegistryService()

    artifact = RegistryArtifact(
        name="ai-api",
        tag="1.0.0",
    )

    assert service.pull(artifact)


def test_delete() -> None:
    service = RegistryService()

    artifact = RegistryArtifact(
        name="ai-api",
        tag="1.0.0",
    )

    assert service.delete(artifact)


def test_invalid_name() -> None:
    service = RegistryService()

    artifact = RegistryArtifact(
        name="",
        tag="1.0.0",
    )

    with pytest.raises(
        RegistryConfigurationError
    ):
        service.publish(artifact)


def test_invalid_tag() -> None:
    service = RegistryService()

    artifact = RegistryArtifact(
        name="ai-api",
        tag="",
    )

    with pytest.raises(
        RegistryConfigurationError
    ):
        service.publish(artifact)


def test_invalid_registry() -> None:
    service = RegistryService()

    artifact = RegistryArtifact(
        name="ai-api",
        tag="1.0.0",
        registry="invalid-registry",
    )

    with pytest.raises(
        RegistryOperationError
    ):
        service.publish(artifact)