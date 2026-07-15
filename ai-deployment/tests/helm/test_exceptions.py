"""
Tests for ai_deployment.helm.exceptions.
"""

from ai_deployment.helm.exceptions import (
    HelmConfigurationError,
    HelmDeploymentError,
    HelmError,
)


def test_helm_error() -> None:
    error = HelmError("error")
    assert str(error) == "error"


def test_configuration_error() -> None:
    assert isinstance(
        HelmConfigurationError("config"),
        HelmError,
    )


def test_deployment_error() -> None:
    assert isinstance(
        HelmDeploymentError("deployment"),
        HelmError,
    )