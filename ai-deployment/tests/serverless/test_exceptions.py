"""
Tests for ai_deployment.serverless.exceptions.
"""

from ai_deployment.serverless.exceptions import (
    ServerlessConfigurationError,
    ServerlessDeploymentError,
    ServerlessError,
)


def test_serverless_error() -> None:
    error = ServerlessError("error")
    assert str(error) == "error"


def test_configuration_error() -> None:
    assert isinstance(
        ServerlessConfigurationError("config"),
        ServerlessError,
    )


def test_deployment_error() -> None:
    assert isinstance(
        ServerlessDeploymentError("deployment"),
        ServerlessError,
    )