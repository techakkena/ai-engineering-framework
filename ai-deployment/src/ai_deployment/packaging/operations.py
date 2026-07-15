"""
Framework-independent packaging operations.
"""

from __future__ import annotations

from dataclasses import dataclass

from ai_deployment.packaging.constants import (
    DEFAULT_BUILD_DIRECTORY,
    DEFAULT_PACKAGE_FORMAT,
    SUPPORTED_PACKAGE_FORMATS,
)
from ai_deployment.packaging.exceptions import (
    PackageBuildError,
    PackagingConfigurationError,
)


@dataclass(slots=True, frozen=True)
class PackageArtifact:
    """Represents a packaged build artifact."""

    name: str
    version: str
    package_format: str = DEFAULT_PACKAGE_FORMAT
    build_directory: str = DEFAULT_BUILD_DIRECTORY


class PackagingService:
    """Framework-independent packaging service."""

    def build(
        self,
        artifact: PackageArtifact,
    ) -> bool:
        """Build a package artifact."""
        if not artifact.name.strip():
            raise PackagingConfigurationError(
                "Package name cannot be empty."
            )

        if artifact.package_format not in SUPPORTED_PACKAGE_FORMATS:
            raise PackagingConfigurationError(
                f"Unsupported package format: "
                f"{artifact.package_format}"
            )

        return True

    def validate(
        self,
        artifact: PackageArtifact,
    ) -> bool:
        """Validate a package artifact."""
        if not artifact.version.strip():
            raise PackageBuildError(
                "Package version cannot be empty."
            )

        return True

    def publish(
        self,
        artifact: PackageArtifact,
    ) -> bool:
        """Publish a package artifact."""
        return self.build(artifact) and self.validate(artifact)