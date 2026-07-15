"""
Exceptions for the Kubernetes module.
"""

from __future__ import annotations


class KubernetesError(Exception):
    """Base exception for Kubernetes operations."""


class KubernetesConfigurationError(KubernetesError):
    """Raised when Kubernetes configuration is invalid."""


class KubernetesDeploymentError(KubernetesError):
    """Raised when deployment operations fail."""