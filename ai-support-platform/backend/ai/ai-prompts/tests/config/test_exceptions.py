from __future__ import annotations

from ai_prompts.config.exceptions import (
    ConfigError,
    InvalidConfigurationError,
    MissingConfigurationError,
)


def test_config_error():
    assert issubclass(
        ConfigError,
        Exception,
    )


def test_invalid_configuration_error():
    assert issubclass(
        InvalidConfigurationError,
        ConfigError,
    )


def test_missing_configuration_error():
    assert issubclass(
        MissingConfigurationError,
        ConfigError,
    )
