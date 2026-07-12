"""
Tests for environment.constants.
"""

from ai_config.environment.constants import (
    DEFAULT_ENCODING,
    DEFAULT_ENV_FILE,
    DEFAULT_ENV_PREFIX,
    FALSE_VALUES,
    TRUE_VALUES,
)


def test_default_encoding() -> None:
    assert DEFAULT_ENCODING == "utf-8"


def test_default_env_file() -> None:
    assert DEFAULT_ENV_FILE == ".env"


def test_default_env_prefix() -> None:
    assert DEFAULT_ENV_PREFIX == ""


def test_true_values() -> None:
    assert "true" in TRUE_VALUES
    assert "1" in TRUE_VALUES
    assert "yes" in TRUE_VALUES
    assert "on" in TRUE_VALUES


def test_false_values() -> None:
    assert "false" in FALSE_VALUES
    assert "0" in FALSE_VALUES
    assert "no" in FALSE_VALUES
    assert "off" in FALSE_VALUES
