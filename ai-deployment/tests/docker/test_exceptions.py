"""
Tests for ai_deployment.docker.exceptions.
"""

from ai_deployment.docker.exceptions import (
    DockerBuildError,
    DockerConfigurationError,
    DockerError,
)


def test_docker_error() -> None:
    error = DockerError("error")
    assert str(error) == "error"


def test_configuration_error() -> None:
    assert isinstance(
        DockerConfigurationError("config"),
        DockerError,
    )


def test_build_error() -> None:
    assert isinstance(
        DockerBuildError("build"),
        DockerError,
    )