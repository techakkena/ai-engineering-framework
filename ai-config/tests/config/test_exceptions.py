"""
Unit tests for config exceptions.
"""

from ai_config.config.exceptions import (
    ConfigError,
    ConfigKeyError,
    ConfigNotLoadedError,
)


def test_config_error() -> None:
    assert isinstance(ConfigError(), Exception)


def test_not_loaded_error() -> None:
    assert isinstance(
        ConfigNotLoadedError(),
        ConfigError,
    )


def test_key_error() -> None:
    assert isinstance(
        ConfigKeyError(),
        ConfigError,
    )
