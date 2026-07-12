"""
Settings operations.

Author: TECHAKKENA
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from ai_config.settings.constants import (
    DEFAULT_COPY_ON_MERGE,
    DEFAULT_SETTINGS,
)
from ai_config.settings.exceptions import SettingNotFoundError


class Settings:
    """
    Represents a mutable configuration object.
    """

    def __init__(
        self,
        values: dict[str, Any] | None = None,
    ) -> None:
        """
        Initialize settings.

        Args:
            values:
                Initial configuration values.
        """
        self._values: dict[str, Any] = (
            deepcopy(values) if values is not None else deepcopy(DEFAULT_SETTINGS)
        )

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Get a configuration value.
        """
        return self._values.get(key, default)

    def require(self, key: str) -> Any:
        """
        Get a required configuration value.

        Raises:
            SettingNotFoundError
        """
        if key not in self._values:
            raise SettingNotFoundError(f"Setting '{key}' not found.")

        return self._values[key]

    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Set a configuration value.
        """
        self._values[key] = value

    def has(self, key: str) -> bool:
        """
        Check whether a key exists.
        """
        return key in self._values

    def remove(self, key: str) -> None:
        """
        Remove a configuration value.
        """
        self._values.pop(key, None)

    def merge(
        self,
        values: dict[str, Any],
    ) -> None:
        """
        Merge configuration values.
        """
        if DEFAULT_COPY_ON_MERGE:
            self._values.update(deepcopy(values))
        else:
            self._values.update(values)

    def clear(self) -> None:
        """
        Remove all configuration values.
        """
        self._values.clear()

    def to_dict(self) -> dict[str, Any]:
        """
        Export configuration.
        """
        return deepcopy(self._values)

    def __len__(self) -> int:
        return len(self._values)

    def __contains__(
        self,
        key: str,
    ) -> bool:
        return key in self._values

    def keys(self) -> list[str]:
        """
        Return all setting keys.
        """
        return list(self._values.keys())

    def values(self) -> list[Any]:
        """
        Return all setting values.
        """
        return list(self._values.values())
