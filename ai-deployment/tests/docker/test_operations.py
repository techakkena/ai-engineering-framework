"""
Tests for ai_deployment.docker.operations.
"""

import pytest

from ai_deployment.docker.exceptions import (
    DockerConfigurationError,
)
from ai_deployment.docker.operations import (
    DockerImage,
    DockerService,
)


def test_build_image() -> None:
    service = DockerService()

    image = service.build("ai-framework")

    assert isinstance(image, DockerImage)
    assert image.repository == "ai-framework"
    assert image.tag == "latest"


def test_full_name() -> None:
    image = DockerImage(
        repository="ai-framework",
        tag="v1.0.0",
    )

    assert (
        image.full_name
        == "docker.io/ai-framework:v1.0.0"
    )


def test_push() -> None:
    service = DockerService()

    image = DockerImage("framework")

    assert service.push(image) is True


def test_pull() -> None:
    service = DockerService()

    image = service.pull("framework")

    assert image.repository == "framework"
    assert image.tag == "latest"


def test_invalid_repository_build() -> None:
    service = DockerService()

    with pytest.raises(DockerConfigurationError):
        service.build("")


def test_invalid_repository_pull() -> None:
    service = DockerService()

    with pytest.raises(DockerConfigurationError):
        service.pull("")


def test_invalid_dockerfile() -> None:
    service = DockerService()

    with pytest.raises(DockerConfigurationError):
        service.build(
            "framework",
            dockerfile="",
        )