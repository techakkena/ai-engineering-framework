"""
Framework-independent registry operations.
"""

from __future__ import annotations

from dataclasses import dataclass

from ai_deployment.registry.constants import (
    DEFAULT_REGISTRY,
    DEFAULT_REPOSITORY,
    SUPPORTED_REGISTRIES,
)
from ai_deployment.registry.exceptions import (
    RegistryConfigurationError,
    RegistryOperationError,
)


@dataclass(slots=True, frozen=True)
class RegistryArtifact:
    """Represents a registry artifact."""

    name: str
    tag: str
    registry: str = DEFAULT_REGISTRY
    repository: str = DEFAULT_REPOSITORY

    @property
    def uri(self) -> str:
        """Return the fully qualified registry URI."""
        return (
            f"{self.registry}/"
            f"{self.repository}/"
            f"{self.name}:{self.tag}"
        )


class RegistryService:
    """Framework-independent registry service."""

    def publish(
        self,
        artifact: RegistryArtifact,
    ) -> bool:
        """Publish an artifact."""
        self._validate(artifact)
        return True

    def pull(
        self,
        artifact: RegistryArtifact,
    ) -> bool:
        """Pull an artifact."""
        self._validate(artifact)
        return True

    def delete(
        self,
        artifact: RegistryArtifact,
    ) -> bool:
        """Delete an artifact."""
        self._validate(artifact)
        return True

    @staticmethod
    def _validate(
        artifact: RegistryArtifact,
    ) -> None:
        """Validate an artifact."""
        if not artifact.name.strip():
            raise RegistryConfigurationError(
                "Artifact name cannot be empty."
            )

        if not artifact.tag.strip():
            raise RegistryConfigurationError(
                "Artifact tag cannot be empty."
            )

        if artifact.registry not in SUPPORTED_REGISTRIES:
            raise RegistryOperationError(
                f"Unsupported registry: "
                f"{artifact.registry}"
            )