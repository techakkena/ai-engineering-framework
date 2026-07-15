"""
Exceptions for the CI/CD module.
"""

from __future__ import annotations


class CICDError(Exception):
    """Base exception for CI/CD operations."""


class CICDConfigurationError(CICDError):
    """Raised when CI/CD configuration is invalid."""


class CICDPipelineError(CICDError):
    """Raised when a pipeline operation fails."""