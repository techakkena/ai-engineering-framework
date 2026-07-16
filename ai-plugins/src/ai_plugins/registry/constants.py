"""Constants for the ai_plugins.registry module."""

from __future__ import annotations

from typing import Final

# Default plugin configuration.
DEFAULT_PLUGIN_NAME: Final[str] = "plugin"
DEFAULT_PLUGIN_VERSION: Final[str] = "1.0.0"
DEFAULT_ENABLED: Final[bool] = True

# Supported plugin states.
REGISTERED_STATE: Final[str] = "registered"
LOADED_STATE: Final[str] = "loaded"
UNLOADED_STATE: Final[str] = "unloaded"
DISABLED_STATE: Final[str] = "disabled"

SUPPORTED_PLUGIN_STATES: Final[frozenset[str]] = frozenset(
    {
        REGISTERED_STATE,
        LOADED_STATE,
        UNLOADED_STATE,
        DISABLED_STATE,
    }
)

# Validation.
MIN_PLUGIN_NAME_LENGTH: Final[int] = 1
MAX_PLUGIN_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
VERSION_KEY: Final[str] = "version"
STATE_KEY: Final[str] = "state"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_ENABLED",
    "DEFAULT_PLUGIN_NAME",
    "DEFAULT_PLUGIN_VERSION",
    "DESCRIPTION_KEY",
    "DISABLED_STATE",
    "ENABLED_KEY",
    "LOADED_STATE",
    "MAX_PLUGIN_NAME_LENGTH",
    "MIN_PLUGIN_NAME_LENGTH",
    "NAME_KEY",
    "REGISTERED_STATE",
    "STATE_KEY",
    "SUPPORTED_PLUGIN_STATES",
    "UNLOADED_STATE",
    "VERSION_KEY",
]