"""
Tests for ai_deployment.packaging.operations.
"""

import pytest

from ai_deployment.packaging.exceptions import (
    PackageBuildError,
    PackagingConfigurationError,
)
from ai_deployment.packaging.operations import (
    PackageArtifact,
    PackagingService,
)


def test_build_package() -> None:
    service = PackagingService()

    artifact = PackageArtifact(
        name="ai-framework",
        version="1.0.0",
    )

    assert service.build(artifact)


def test_validate_package() -> None:
    service = PackagingService()

    artifact = PackageArtifact(
        name="ai-framework",
        version="1.0.0",
    )

    assert service.validate(artifact)


def test_publish_package() -> None:
    service = PackagingService()

    artifact = PackageArtifact(
        name="ai-framework",
        version="1.0.0",
    )

    assert service.publish(artifact)


def test_invalid_package_name() -> None:
    service = PackagingService()

    artifact = PackageArtifact(
        name="",
        version="1.0.0",
    )

    with pytest.raises(PackagingConfigurationError):
        service.build(artifact)


def test_invalid_package_format() -> None:
    service = PackagingService()

    artifact = PackageArtifact(
        name="ai-framework",
        version="1.0.0",
        package_format="invalid",
    )

    with pytest.raises(PackagingConfigurationError):
        service.build(artifact)


def test_invalid_version() -> None:
    service = PackagingService()

    artifact = PackageArtifact(
        name="ai-framework",
        version="",
    )

    with pytest.raises(PackageBuildError):
        service.validate(artifact)