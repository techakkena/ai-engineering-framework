"""
Tests for ai_deployment.kubernetes.operations.
"""

import pytest

from ai_deployment.kubernetes.exceptions import (
    KubernetesConfigurationError,
    KubernetesDeploymentError,
)
from ai_deployment.kubernetes.operations import (
    KubernetesDeployment,
    KubernetesService,
)


def test_deploy() -> None:
    service = KubernetesService()

    deployment = KubernetesDeployment(
        name="ai-api",
        image="ai-api:latest",
    )

    assert service.deploy(deployment)


def test_scale() -> None:
    service = KubernetesService()

    deployment = KubernetesDeployment(
        name="ai-api",
        image="ai-api:latest",
    )

    scaled = service.scale(
        deployment,
        replicas=3,
    )

    assert scaled.replicas == 3
    assert scaled.name == deployment.name
    assert scaled.image == deployment.image


def test_delete() -> None:
    service = KubernetesService()

    assert service.delete("ai-api")


def test_invalid_deployment_name() -> None:
    service = KubernetesService()

    deployment = KubernetesDeployment(
        name="",
        image="image",
    )

    with pytest.raises(KubernetesConfigurationError):
        service.deploy(deployment)


def test_invalid_image() -> None:
    service = KubernetesService()

    deployment = KubernetesDeployment(
        name="api",
        image="",
    )

    with pytest.raises(KubernetesConfigurationError):
        service.deploy(deployment)


def test_invalid_scale() -> None:
    service = KubernetesService()

    deployment = KubernetesDeployment(
        name="api",
        image="image",
    )

    with pytest.raises(KubernetesDeploymentError):
        service.scale(
            deployment,
            replicas=0,
        )


def test_invalid_delete() -> None:
    service = KubernetesService()

    with pytest.raises(KubernetesConfigurationError):
        service.delete("")