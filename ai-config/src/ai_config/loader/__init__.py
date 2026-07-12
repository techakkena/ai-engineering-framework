"""
Configuration loader.

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
from ai_config.loader.exceptions import (
    ConfigurationNotFoundError,
    ConfigurationParseError,
    LoaderError,
    UnsupportedFormatError,
)
from ai_config.loader.operations import (
    detect_loader,
    is_supported,
    load_config,
    load_env,
    load_json,
    load_toml,
    load_yaml,
)

__all__ = [
    "DEFAULT_CACHE_SIZE",
    "DEFAULT_ENCODING",
    "ENV_EXTENSION",
    "JSON_EXTENSION",
    "SUPPORTED_EXTENSIONS",
    "TOML_EXTENSION",
    "YAML_EXTENSIONS",
    "LoaderError",
    "UnsupportedFormatError",
    "ConfigurationNotFoundError",
    "ConfigurationParseError",
    "detect_loader",
    "is_supported",
    "load_config",
    "load_env",
    "load_json",
    "load_toml",
    "load_yaml",
]
