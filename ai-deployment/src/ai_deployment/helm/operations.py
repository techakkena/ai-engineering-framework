"""
Framework-independent Helm operations.
"""

from __future__ import annotations

from dataclasses import dataclass

from ai_deployment.helm.constants import (
    DEFAULT_CHART_VERSION,
    DEFAULT_NAMESPACE,
    DEFAULT_RELEASE_NAME,
)
from ai_deployment.helm.exceptions import (
    HelmConfigurationError,
    HelmDeploymentError,
)


@dataclass(slots=True, frozen=True)
class HelmChart:
    """Represents a Helm chart."""

    chart: str
    version: str = DEFAULT_CHART_VERSION
    release: str = DEFAULT_RELEASE_NAME
    namespace: str = DEFAULT_NAMESPACE


class HelmService:
    """Framework-independent Helm service."""

    def install(self, chart: HelmChart) -> bool:
        """Install a Helm chart."""
        if not chart.chart.strip():
            raise HelmConfigurationError(
                "Chart name cannot be empty."
            )

        return True

    def upgrade(self, chart: HelmChart) -> bool:
        """Upgrade a Helm release."""
        if not chart.release.strip():
            raise HelmDeploymentError(
                "Release name cannot be empty."
            )

        return True

    def uninstall(self, release: str) -> bool:
        """Uninstall a Helm release."""
        if not release.strip():
            raise HelmConfigurationError(
                "Release name cannot be empty."
            )

        return True