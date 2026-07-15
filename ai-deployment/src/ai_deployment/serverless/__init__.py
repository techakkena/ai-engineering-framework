"""
Framework-independent serverless deployment abstractions.

This package provides interfaces and utilities for deploying AI
applications to serverless platforms such as AWS Lambda, Azure
Functions, Google Cloud Functions, and Cloud Run.
"""

from ai_deployment.serverless.constants import (
    DEFAULT_MEMORY_MB,
    DEFAULT_RUNTIME,
    DEFAULT_TIMEOUT_SECONDS,
)
from ai_deployment.serverless.exceptions import (
    ServerlessConfigurationError,
    ServerlessDeploymentError,
    ServerlessError,
)
from ai_deployment.serverless.operations import (
    ServerlessFunction,
    ServerlessService,
)

__all__ = [
    "DEFAULT_MEMORY_MB",
    "DEFAULT_RUNTIME",
    "DEFAULT_TIMEOUT_SECONDS",
    "ServerlessConfigurationError",
    "ServerlessDeploymentError",
    "ServerlessError",
    "ServerlessFunction",
    "ServerlessService",
]