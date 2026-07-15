"""
Exceptions for the Docker module.
"""

from __future__ import annotations


class DockerError(Exception):
    """Base exception for Docker operations."""


class DockerConfigurationError(DockerError):
    """Raised when Docker configuration is invalid."""


class DockerBuildError(DockerError):
    """Raised when a Docker build operation fails."""