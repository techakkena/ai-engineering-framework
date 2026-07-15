"""
Framework-independent release operations.
"""

from __future__ import annotations

from dataclasses import dataclass

from ai_deployment.release.constants import (
    DEFAULT_RELEASE_CHANNEL,
    DEFAULT_VERSION_PREFIX,
    SUPPORTED_RELEASE_CHANNELS,
)
from ai_deployment.release.exceptions import (
    ReleaseConfigurationError,
    ReleaseValidationError,
)


@dataclass(slots=True, frozen=True)
class Release:
    """Represents a software release."""

    version: str
    channel: str = DEFAULT_RELEASE_CHANNEL
    version_prefix: str = DEFAULT_VERSION_PREFIX

    @property
    def full_version(self) -> str:
        """Return the formatted release version."""
        return f"{self.version_prefix}{self.version}"


class ReleaseService:
    """Framework-independent release service."""

    def validate(self, release: Release) -> bool:
        """Validate a release."""
        if not release.version.strip():
            raise ReleaseValidationError(
                "Release version cannot be empty."
            )

        if release.channel not in SUPPORTED_RELEASE_CHANNELS:
            raise ReleaseConfigurationError(
                f"Unsupported release channel: "
                f"{release.channel}"
            )

        return True

    def publish(self, release: Release) -> bool:
        """Publish a release."""
        return self.validate(release)

    def rollback(self, release: Release) -> bool:
        """Rollback a release."""
        return self.validate(release)