"""Operations for the ai_optimization.profiling module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_optimization.profiling.constants import (
    DEFAULT_ENABLED,
    DEFAULT_PROFILE_TYPE,
    MAX_PROFILE_NAME_LENGTH,
    MIN_PROFILE_NAME_LENGTH,
    SUPPORTED_PROFILE_TYPES,
)
from ai_optimization.profiling.exceptions import (
    DuplicateProfileError,
    ProfileNotFoundError,
    ProfileValidationError,
    UnsupportedProfileTypeError,
)


@dataclass(slots=True, frozen=True)
class ProfileDefinition:
    """Represents a profiling configuration."""

    name: str
    interval: float
    profile_type: str = DEFAULT_PROFILE_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the profile definition."""
        normalized = self.name.strip()

        if not (
            MIN_PROFILE_NAME_LENGTH
            <= len(normalized)
            <= MAX_PROFILE_NAME_LENGTH
        ):
            raise ProfileValidationError(
                "Profile name length is outside the allowed range."
            )

        if self.interval <= 0:
            raise ProfileValidationError(
                "Profile interval must be greater than zero."
            )

        if self.profile_type not in SUPPORTED_PROFILE_TYPES:
            raise UnsupportedProfileTypeError(
                f"Unsupported profile type: {self.profile_type!r}."
            )

        object.__setattr__(self, "name", normalized)


class ProfileRegistry:
    """Registry for profile definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, ProfileDefinition] = {}

    def register(self, profile: ProfileDefinition) -> None:
        """Register a profile definition."""
        if profile.name in self._definitions:
            raise DuplicateProfileError(
                f"Profile {profile.name!r} is already registered."
            )

        self._definitions[profile.name] = profile

    def unregister(self, name: str) -> None:
        """Remove a profile definition."""
        if name not in self._definitions:
            raise ProfileNotFoundError(
                f"Profile {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> ProfileDefinition:
        """Return a registered profile definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise ProfileNotFoundError(
                f"Profile {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a profile exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered profiles."""
        self._definitions.clear()

    def list(self) -> tuple[ProfileDefinition, ...]:
        """Return all registered profiles."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return the number of registered profiles."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a profile exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_profile(
    *,
    name: str,
    interval: float,
    profile_type: str = DEFAULT_PROFILE_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> ProfileDefinition:
    """Build and validate a profile definition."""
    return ProfileDefinition(
        name=name,
        interval=interval,
        profile_type=profile_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "ProfileDefinition",
    "ProfileRegistry",
    "build_profile",
]