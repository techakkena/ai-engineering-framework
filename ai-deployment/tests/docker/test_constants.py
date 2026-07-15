"""
Tests for ai_deployment.docker.constants.
"""

from ai_deployment.docker.constants import (
    DEFAULT_DOCKERFILE,
    DEFAULT_IMAGE_TAG,
    DEFAULT_REGISTRY,
)


def test_default_dockerfile() -> None:
    assert DEFAULT_DOCKERFILE == "Dockerfile"


def test_default_image_tag() -> None:
    assert DEFAULT_IMAGE_TAG == "latest"


def test_default_registry() -> None:
    assert DEFAULT_REGISTRY == "docker.io"