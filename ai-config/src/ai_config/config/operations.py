"""
Configuration manager.

Author: TECHAKKENA
"""

from __future__ import annotations

from typing import Any

from ai_config.profiles.operations import ProfileManager
from ai_config.settings.operations import Settings


class Config:
    """
    High-level configuration interface.
    """

    def __init__(self) -> None:
        self.settings = Settings()
        self.profiles = ProfileManager()

    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store a configuration value.
        """
        self.settings.set(key, value)

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve a configuration value.
        """
        return self.settings.get(key, default)

    def remove(
        self,
        key: str,
    ) -> None:
        """
        Remove a configuration value.
        """
        self.settings.remove(key)

    def clear(self) -> None:
        """
        Remove all configuration values.
        """
        self.settings.clear()

    def keys(self) -> list[str]:
        """
        Return all keys.
        """
        return self.settings.keys()

    def values(self) -> list[Any]:
        """
        Return all values.
        """
        return self.settings.values()

    def items(self) -> dict[str, Any]:
        """
        Return configuration dictionary.
        """
        return self.settings.to_dict()

    def profile(self) -> str:
        """
        Return active profile.
        """
        return self.profiles.active_profile()
