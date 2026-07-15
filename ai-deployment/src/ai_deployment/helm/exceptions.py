"""
Exceptions for the Helm module.
"""

from __future__ import annotations


class HelmError(Exception):
    """Base exception for Helm operations."""


class HelmConfigurationError(HelmError):
    """Raised when Helm configuration is invalid."""


class HelmDeploymentError(HelmError):
    """Raised when a Helm deployment operation fails."""