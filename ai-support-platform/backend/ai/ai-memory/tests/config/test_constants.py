from __future__ import annotations

"""Tests for ai_memory.config.constants."""

from ai_memory.config.constants import (
    ConfigFormat,
    ConfigScope,
    DEFAULT_CONFIG_FILE,
    DEFAULT_CONFIG_NAMESPACE,
)


def test_config_format_values() -> None:
    assert ConfigFormat.JSON.value == "json"
    assert ConfigFormat.YAML.value == "yaml"
    assert ConfigFormat.TOML.value == "toml"
    assert ConfigFormat.ENV.value == "env"


def test_config_scope_values() -> None:
    assert ConfigScope.GLOBAL.value == "global"
    assert ConfigScope.MEMORY.value == "memory"
    assert ConfigScope.SESSION.value == "session"
    assert ConfigScope.USER.value == "user"


def test_default_values() -> None:
    assert DEFAULT_CONFIG_FILE == "memory.toml"
    assert DEFAULT_CONFIG_NAMESPACE == "default"
