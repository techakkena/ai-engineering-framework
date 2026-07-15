"""
Tests for ai_deployment.kubernetes.exceptions.
"""

from ai_deployment.kubernetes.exceptions import (
    KubernetesConfigurationError,
    KubernetesDeploymentError,
    KubernetesError,
)


def test_kubernetes_error() -> None:
    error = KubernetesError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    assert isinstance(
        KubernetesConfigurationError("config"),
        KubernetesError,
    )


def test_deployment_error() -> None:
    assert isinstance(
        KubernetesDeploymentError("deployment"),
        KubernetesError,
    )