"""Operations for the ai_cloud.deployment module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_cloud.deployment.constants import (
    DEFAULT_DEPLOYMENT_STRATEGY,
    DEFAULT_ENABLED,
    MAX_DEPLOYMENT_NAME_LENGTH,
    MIN_DEPLOYMENT_NAME_LENGTH,
    SUPPORTED_DEPLOYMENT_STRATEGIES,
)
from ai_cloud.deployment.exceptions import (
    DeploymentNotFoundError,
    DeploymentValidationError,
    DuplicateDeploymentError,
    UnsupportedDeploymentStrategyError,
)


@dataclass(slots=True, frozen=True)
class DeploymentDefinition:
    """Represents a cloud deployment configuration."""

    name: str
    replicas: int
    strategy: str = DEFAULT_DEPLOYMENT_STRATEGY
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the deployment definition."""
        normalized = self.name.strip()

        if not (
            MIN_DEPLOYMENT_NAME_LENGTH
            <= len(normalized)
            <= MAX_DEPLOYMENT_NAME_LENGTH
        ):
            raise DeploymentValidationError(
                "Deployment name length is outside the allowed range."
            )

        if self.replicas <= 0:
            raise DeploymentValidationError(
                "Replica count must be greater than zero."
            )

        if (
            self.strategy
            not in SUPPORTED_DEPLOYMENT_STRATEGIES
        ):
            raise UnsupportedDeploymentStrategyError(
                f"Unsupported deployment strategy: {self.strategy!r}."
            )

        object.__setattr__(self, "name", normalized)


class DeploymentRegistry:
    """Registry for deployment definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        self._definitions: dict[
            str,
            DeploymentDefinition,
        ] = {}

    def register(
        self,
        deployment: DeploymentDefinition,
    ) -> None:
        if deployment.name in self._definitions:
            raise DuplicateDeploymentError(
                f"Deployment {deployment.name!r} is already registered."
            )

        self._definitions[deployment.name] = deployment

    def unregister(self, name: str) -> None:
        if name not in self._definitions:
            raise DeploymentNotFoundError(
                f"Deployment {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> DeploymentDefinition:
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise DeploymentNotFoundError(
                f"Deployment {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        return name in self._definitions

    def clear(self) -> None:
        self._definitions.clear()

    def list(
        self,
    ) -> tuple[
        DeploymentDefinition,
        ...,
    ]:
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_deployment(
    *,
    name: str,
    replicas: int,
    strategy: str = DEFAULT_DEPLOYMENT_STRATEGY,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> DeploymentDefinition:
    """Build a validated deployment definition."""

    return DeploymentDefinition(
        name=name,
        replicas=replicas,
        strategy=strategy,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "DeploymentDefinition",
    "DeploymentRegistry",
    "build_deployment",
]