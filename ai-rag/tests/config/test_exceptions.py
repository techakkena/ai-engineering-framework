from ai_rag.config.exceptions import (
    ConfigError,
    InvalidConfigError,
    MissingConfigError,
)


def test_config_error():
    assert issubclass(
        ConfigError,
        Exception,
    )


def test_invalid_config_error():
    assert issubclass(
        InvalidConfigError,
        ConfigError,
    )


def test_missing_config_error():
    assert issubclass(
        MissingConfigError,
        ConfigError,
    )