"""
Tests for ai_deployment.registry.constants.
"""

from ai_deployment.registry.constants import (
    DEFAULT_REGISTRY,
    DEFAULT_REPOSITORY,
    SUPPORTED_REGISTRIES,
)


def test_default_registry() -> None:
    assert DEFAULT_REGISTRY == "docker.io"


def test_default_repository() -> None:
    assert DEFAULT_REPOSITORY == "library"


def test_supported_registries() -> None:
    assert "docker.io" in SUPPORTED_REGISTRIES
    assert "ghcr.io" in SUPPORTED_REGISTRIES
    assert "gcr.io" in SUPPORTED_REGISTRIES