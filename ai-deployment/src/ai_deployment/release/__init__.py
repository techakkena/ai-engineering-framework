"""
Release management for the AI Engineering Framework.

This package provides framework-independent abstractions for release
creation, validation, and publication.
"""

from ai_deployment.release.constants import (
    DEFAULT_RELEASE_CHANNEL,
    DEFAULT_VERSION_PREFIX,
    SUPPORTED_RELEASE_CHANNELS,
)
from ai_deployment.release.exceptions import (
    ReleaseConfigurationError,
    ReleaseError,
    ReleaseValidationError,
)
from ai_deployment.release.operations import (
    Release,
    ReleaseService,
)

__all__ = [
    "DEFAULT_RELEASE_CHANNEL",
    "DEFAULT_VERSION_PREFIX",
    "SUPPORTED_RELEASE_CHANNELS",
    "ReleaseConfigurationError",
    "ReleaseError",
    "ReleaseValidationError",
    "Release",
    "ReleaseService",
]