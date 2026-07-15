"""
Framework-independent serverless deployment operations.
"""

from __future__ import annotations

from dataclasses import dataclass

from ai_deployment.serverless.constants import (
    DEFAULT_MEMORY_MB,
    DEFAULT_RUNTIME,
    DEFAULT_TIMEOUT_SECONDS,
)
from ai_deployment.serverless.exceptions import (
    ServerlessConfigurationError,
    ServerlessDeploymentError,
)


@dataclass(slots=True, frozen=True)
class ServerlessFunction:
    """Represents a serverless function."""

    name: str
    runtime: str = DEFAULT_RUNTIME
    memory_mb: int = DEFAULT_MEMORY_MB
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS


class ServerlessService:
    """Framework-independent serverless deployment service."""

    def deploy(
        self,
        function: ServerlessFunction,
    ) -> bool:
        """Deploy a serverless function."""
        if not function.name.strip():
            raise ServerlessConfigurationError(
                "Function name cannot be empty."
            )

        if function.memory_mb <= 0:
            raise ServerlessConfigurationError(
                "Memory must be greater than zero."
            )

        if function.timeout_seconds <= 0:
            raise ServerlessConfigurationError(
                "Timeout must be greater than zero."
            )

        return True

    def update(
        self,
        function: ServerlessFunction,
    ) -> bool:
        """Update an existing function."""
        return self.deploy(function)

    def delete(
        self,
        name: str,
    ) -> bool:
        """Delete a serverless function."""
        if not name.strip():
            raise ServerlessDeploymentError(
                "Function name cannot be empty."
            )

        return True