"""
Framework-independent Kubernetes operations.
"""

from __future__ import annotations

from dataclasses import dataclass

from ai_deployment.kubernetes.constants import (
    DEFAULT_NAMESPACE,
    DEFAULT_REPLICAS,
    DEFAULT_SERVICE_TYPE,
)
from ai_deployment.kubernetes.exceptions import (
    KubernetesConfigurationError,
    KubernetesDeploymentError,
)


@dataclass(slots=True, frozen=True)
class KubernetesDeployment:
    """Represents a Kubernetes deployment."""

    name: str
    image: str
    namespace: str = DEFAULT_NAMESPACE
    replicas: int = DEFAULT_REPLICAS
    service_type: str = DEFAULT_SERVICE_TYPE


class KubernetesService:
    """Framework-independent Kubernetes service."""

    def deploy(
        self,
        deployment: KubernetesDeployment,
    ) -> bool:
        """Deploy an application."""
        if not deployment.name.strip():
            raise KubernetesConfigurationError(
                "Deployment name cannot be empty."
            )

        if not deployment.image.strip():
            raise KubernetesConfigurationError(
                "Container image cannot be empty."
            )

        return True

    def scale(
        self,
        deployment: KubernetesDeployment,
        replicas: int,
    ) -> KubernetesDeployment:
        """Scale a deployment."""
        if replicas < 1:
            raise KubernetesDeploymentError(
                "Replicas must be greater than zero."
            )

        return KubernetesDeployment(
            name=deployment.name,
            image=deployment.image,
            namespace=deployment.namespace,
            replicas=replicas,
            service_type=deployment.service_type,
        )

    def delete(
        self,
        name: str,
    ) -> bool:
        """Delete a deployment."""
        if not name.strip():
            raise KubernetesConfigurationError(
                "Deployment name cannot be empty."
            )

        return True