"""
Unit tests for loader operations.

Author: TECHAKKENA
"""

import pytest

from ai_config.loader.exceptions import UnsupportedFormatError
from ai_config.loader.operations import (
    detect_loader,
    is_supported,
    load_config,
)


def test_is_supported_json() -> None:
    """Test JSON support."""
    assert is_supported("config.json")


def test_is_supported_yaml() -> None:
    """Test YAML support."""
    assert is_supported("config.yaml")
    assert is_supported("config.yml")


def test_is_supported_toml() -> None:
    """Test TOML support."""
    assert is_supported("config.toml")


def test_is_supported_env() -> None:
    """Test ENV support."""
    assert is_supported(".env")


def test_is_not_supported() -> None:
    """Test unsupported extension."""
    assert not is_supported("config.xml")


def test_detect_json() -> None:
    """Test JSON detection."""
    assert detect_loader("config.json") == ".json"


def test_detect_yaml() -> None:
    """Test YAML detection."""
    assert detect_loader("config.yaml") == ".yaml"


def test_detect_yml() -> None:
    """Test YML detection."""
    assert detect_loader("config.yml") == ".yml"


def test_detect_toml() -> None:
    """Test TOML detection."""
    assert detect_loader("config.toml") == ".toml"


def test_detect_env() -> None:
    """Test ENV detection."""
    assert detect_loader(".env") == ".env"


def test_detect_invalid_extension() -> None:
    """Test unsupported extension detection."""
    with pytest.raises(UnsupportedFormatError):
        detect_loader("config.xml")


def test_load_config_invalid_extension() -> None:
    """Test load_config() with unsupported format."""
    with pytest.raises(UnsupportedFormatError):
        load_config("config.xml")


def test_load_config_json_not_implemented() -> None:
    """Test JSON loader placeholder."""
    with pytest.raises(NotImplementedError):
        load_config("config.json")


def test_load_config_yaml_not_implemented() -> None:
    """Test YAML loader placeholder."""
    with pytest.raises(NotImplementedError):
        load_config("config.yaml")


def test_load_config_toml_not_implemented() -> None:
    """Test TOML loader placeholder."""
    with pytest.raises(NotImplementedError):
        load_config("config.toml")


def test_load_config_env_not_implemented() -> None:
    """Test ENV loader placeholder."""
    with pytest.raises(NotImplementedError):
        load_config(".env")
