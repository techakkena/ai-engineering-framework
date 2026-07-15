"""
Framework-independent semantic versioning operations.
"""

from __future__ import annotations

from dataclasses import dataclass

from ai_deployment.versioning.constants import (
    DEFAULT_INITIAL_VERSION,
)


@dataclass(slots=True, frozen=True, order=True)
class SemanticVersion:
    """Represents a semantic version."""

    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        """Return the semantic version string."""
        return f"{self.major}.{self.minor}.{self.patch}"


class VersionService:
    """Framework-independent semantic version service."""

    @staticmethod
    def parse(version: str) -> SemanticVersion:
        """Parse a semantic version."""
        parts = version.split(".")

        if len(parts) != 3:
            raise ValueError(
                "Version must contain major.minor.patch."
            )

        return SemanticVersion(
            major=int(parts[0]),
            minor=int(parts[1]),
            patch=int(parts[2]),
        )

    @staticmethod
    def initial() -> SemanticVersion:
        """Return the default initial version."""
        return VersionService.parse(DEFAULT_INITIAL_VERSION)

    @staticmethod
    def bump_major(
        version: SemanticVersion,
    ) -> SemanticVersion:
        """Increment the major version."""
        return SemanticVersion(
            version.major + 1,
            0,
            0,
        )

    @staticmethod
    def bump_minor(
        version: SemanticVersion,
    ) -> SemanticVersion:
        """Increment the minor version."""
        return SemanticVersion(
            version.major,
            version.minor + 1,
            0,
        )

    @staticmethod
    def bump_patch(
        version: SemanticVersion,
    ) -> SemanticVersion:
        """Increment the patch version."""
        return SemanticVersion(
            version.major,
            version.minor,
            version.patch + 1,
        )