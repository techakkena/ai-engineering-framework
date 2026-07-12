"""
Configuration loading operations.

Author: TECHAKKENA
"""

from pathlib import Path
from typing import Any

from ai_config.loader.constants import (
    ENV_EXTENSION,
    JSON_EXTENSION,
    SUPPORTED_EXTENSIONS,
    TOML_EXTENSION,
    YAML_EXTENSIONS,
)
from ai_config.loader.exceptions import UnsupportedFormatError


def is_supported(path: str | Path) -> bool:
    """
    Check whether a configuration file extension is supported.

    Args:
        path: Configuration file path.

    Returns:
        True if supported, otherwise False.
    """
    path = Path(path)

    if path.name == ".env":
        return True

    return path.suffix.lower() in SUPPORTED_EXTENSIONS


def detect_loader(path: str | Path) -> str:
    """
    Detect the configuration file type.

    Args:
        path: Configuration file path.

    Returns:
        File extension.

    Raises:
        UnsupportedFormatError:
            If the file extension is not supported.
    """
    path = Path(path)

    if path.name == ".env":
        return ENV_EXTENSION

    extension = path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise UnsupportedFormatError(f"Unsupported configuration format: {extension}")

    return extension


def load_json(path: str | Path) -> dict[str, Any]:
    """
    Placeholder for JSON loader.
    """
    raise NotImplementedError


def load_yaml(path: str | Path) -> dict[str, Any]:
    """
    Placeholder for YAML loader.
    """
    raise NotImplementedError


def load_toml(path: str | Path) -> dict[str, Any]:
    """
    Placeholder for TOML loader.
    """
    raise NotImplementedError


def load_env(path: str | Path) -> dict[str, Any]:
    """
    Placeholder for ENV loader.
    """
    raise NotImplementedError


def load_config(path: str | Path) -> dict[str, Any]:
    """
    Load configuration from a supported file.

    Args:
        path: Configuration file path.

    Returns:
        Configuration dictionary.

    Raises:
        UnsupportedFormatError:
            If the configuration format is unsupported.
    """
    extension = detect_loader(path)

    if extension == JSON_EXTENSION:
        return load_json(path)

    if extension in YAML_EXTENSIONS:
        return load_yaml(path)

    if extension == TOML_EXTENSION:
        return load_toml(path)

    if extension == ENV_EXTENSION:
        return load_env(path)

    raise UnsupportedFormatError(f"Unsupported configuration format: {extension}")
