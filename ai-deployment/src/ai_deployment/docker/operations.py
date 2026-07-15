"""
Framework-independent Docker operations.
"""

from __future__ import annotations

from dataclasses import dataclass

from ai_deployment.docker.constants import (
    DEFAULT_DOCKERFILE,
    DEFAULT_IMAGE_TAG,
    DEFAULT_REGISTRY,
)
from ai_deployment.docker.exceptions import (
    DockerBuildError,
    DockerConfigurationError,
)


@dataclass(slots=True, frozen=True)
class DockerImage:
    """Represents a Docker image."""

    repository: str
    tag: str = DEFAULT_IMAGE_TAG
    registry: str = DEFAULT_REGISTRY

    @property
    def full_name(self) -> str:
        """Return the fully qualified image name."""
        return f"{self.registry}/{self.repository}:{self.tag}"


class DockerService:
    """Framework-independent Docker service."""

    def build(
        self,
        repository: str,
        *,
        dockerfile: str = DEFAULT_DOCKERFILE,
        tag: str = DEFAULT_IMAGE_TAG,
    ) -> DockerImage:
        """Build a Docker image."""
        if not repository.strip():
            raise DockerConfigurationError(
                "Repository cannot be empty."
            )

        if not dockerfile.strip():
            raise DockerConfigurationError(
                "Dockerfile cannot be empty."
            )

        return DockerImage(
            repository=repository,
            tag=tag,
        )

    def push(
        self,
        image: DockerImage,
    ) -> bool:
        """Push an image.

        Placeholder implementation.
        """
        if not image.repository:
            raise DockerBuildError(
                "Invalid Docker image."
            )

        return True

    def pull(
        self,
        repository: str,
        *,
        tag: str = DEFAULT_IMAGE_TAG,
    ) -> DockerImage:
        """Pull an image.

        Placeholder implementation.
        """
        if not repository.strip():
            raise DockerConfigurationError(
                "Repository cannot be empty."
            )

        return DockerImage(
            repository=repository,
            tag=tag,
        )