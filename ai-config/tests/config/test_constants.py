"""
Unit tests for config constants.
"""

from ai_config.config.constants import (
    DEFAULT_CONFIG_FILE,
    DEFAULT_ENCODING,
    DEFAULT_PROFILE_NAME,
)


def test_default_config_file() -> None:
    assert DEFAULT_CONFIG_FILE == "config.toml"


def test_default_encoding() -> None:
    assert DEFAULT_ENCODING == "utf-8"


def test_default_profile() -> None:
    assert DEFAULT_PROFILE_NAME == "default"
