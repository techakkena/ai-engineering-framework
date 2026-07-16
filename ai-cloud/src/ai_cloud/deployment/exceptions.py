"""Exceptions for the ai_cloud.deployment module."""

from __future__ import annotations


class DeploymentError(Exception):
    """Base exception for deployment operations."""


class DeploymentValidationError(DeploymentError):
    """Raised when deployment validation fails."""


class DeploymentRegistrationError(DeploymentError):
    """Raised when deployment registration fails."""


class DeploymentNotFoundError(
    DeploymentRegistrationError,
):
    """Raised when a deployment definition cannot be found."""


class DuplicateDeploymentError(
    DeploymentRegistrationError,
):
    """Raised when attempting to register a duplicate deployment."""


class UnsupportedDeploymentStrategyError(
    DeploymentValidationError,
):
    """Raised when an unsupported deployment strategy is specified."""


__all__ = [
    "DeploymentError",
    "DeploymentNotFoundError",
    "DeploymentRegistrationError",
    "DeploymentValidationError",
    "DuplicateDeploymentError",
    "UnsupportedDeploymentStrategyError",
]