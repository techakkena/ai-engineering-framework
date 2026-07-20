from __future__ import annotations

"""Constants for the ai_memory.config module."""

from __future__ import annotations

from enum import Enum


class ConfigFormat(str, Enum):
    """Supported configuration formats."""

    JSON = "json"
    YAML = "yaml"
    TOML = "toml"
    ENV = "env"


class ConfigScope(str, Enum):
    """Configuration scopes."""

    GLOBAL = "global"
    MEMORY = "memory"
    SESSION = "session"
    USER = "user"


DEFAULT_CONFIG_FILE = "memory.toml"
DEFAULT_CONFIG_NAMESPACE = "default"
