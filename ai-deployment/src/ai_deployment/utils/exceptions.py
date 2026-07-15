"""
Exceptions for ai_deployment.utils.
"""

from __future__ import annotations


class DeploymentUtilityError(Exception):
    """Base exception for deployment utility operations."""


class ValidationError(DeploymentUtilityError):
    """Raised when deployment validation fails."""