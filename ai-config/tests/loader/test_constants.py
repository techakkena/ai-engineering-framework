"""
Unit tests for loader constants.

Author: TECHAKKENA
"""

from ai_config.loader.constants import (
    DEFAULT_CACHE_SIZE,
    DEFAULT_ENCODING,
    ENV_EXTENSION,
    JSON_EXTENSION,
    SUPPORTED_EXTENSIONS,
    TOML_EXTENSION,
    YAML_EXTENSIONS,
)


def test_default_encoding() -> None:
    """Test the default encoding."""
    assert DEFAULT_ENCODING == "utf-8"


def test_default_cache_size() -> None:
    """Test the default cache size."""
    assert DEFAULT_CACHE_SIZE == 128


def test_env_extension() -> None:
    """Test the environment extension."""
    assert ENV_EXTENSION == ".env"


def test_json_extension() -> None:
    """Test the JSON extension."""
    assert JSON_EXTENSION == ".json"


def test_yaml_extensions() -> None:
    """Test the YAML extensions."""
    assert YAML_EXTENSIONS == (".yaml", ".yml")


def test_toml_extension() -> None:
    """Test the TOML extension."""
    assert TOML_EXTENSION == ".toml"


def test_supported_extensions() -> None:
    """Test supported extensions."""
    assert ENV_EXTENSION in SUPPORTED_EXTENSIONS
    assert JSON_EXTENSION in SUPPORTED_EXTENSIONS
    assert TOML_EXTENSION in SUPPORTED_EXTENSIONS
    assert ".yaml" in SUPPORTED_EXTENSIONS
    assert ".yml" in SUPPORTED_EXTENSIONS
