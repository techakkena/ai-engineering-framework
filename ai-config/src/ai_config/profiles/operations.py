"""
Profile operations.

Author: TECHAKKENA
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from ai_config.profiles.constants import DEFAULT_PROFILE
from ai_config.profiles.exceptions import (
    DuplicateProfileError,
    ProfileNotFoundError,
)


class ProfileManager:
    """
    Manage configuration profiles.
    """

    def __init__(self) -> None:
        self._profiles: dict[str, dict[str, Any]] = {DEFAULT_PROFILE: {}}
        self._active = DEFAULT_PROFILE

    def add(
        self,
        name: str,
        values: dict[str, Any] | None = None,
    ) -> None:
        """
        Add a profile.
        """
        if name in self._profiles:
            raise DuplicateProfileError(f"Profile '{name}' already exists.")

        self._profiles[name] = deepcopy(values or {})

    def get(
        self,
        name: str,
    ) -> dict[str, Any]:
        """
        Get profile values.
        """
        if name not in self._profiles:
            raise ProfileNotFoundError(f"Profile '{name}' not found.")

        return deepcopy(self._profiles[name])

    def remove(
        self,
        name: str,
    ) -> None:
        """
        Remove a profile.
        """
        if name == DEFAULT_PROFILE:
            return

        self._profiles.pop(name, None)

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check whether a profile exists.
        """
        return name in self._profiles

    def list(self) -> list[str]:
        """
        Return profile names.
        """
        return sorted(self._profiles.keys())

    def activate(
        self,
        name: str,
    ) -> None:
        """
        Activate a profile.
        """
        if name not in self._profiles:
            raise ProfileNotFoundError(f"Profile '{name}' not found.")

        self._active = name

    def active_profile(self) -> str:
        """
        Return the active profile.
        """
        return self._active

    def clear(self) -> None:
        """
        Remove all profiles except default.
        """
        self._profiles = {DEFAULT_PROFILE: {}}
        self._active = DEFAULT_PROFILE

    def to_dict(self) -> dict[str, dict[str, Any]]:
        """
        Export profiles.
        """
        return deepcopy(self._profiles)
