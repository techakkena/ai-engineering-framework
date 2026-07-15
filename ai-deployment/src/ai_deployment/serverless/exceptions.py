"""
Exceptions for the serverless module.
"""

from __future__ import annotations


class ServerlessError(Exception):
    """Base exception for serverless operations."""


class ServerlessConfigurationError(ServerlessError):
    """Raised when serverless configuration is invalid."""


class ServerlessDeploymentError(ServerlessError):
    """Raised when a deployment operation fails."""