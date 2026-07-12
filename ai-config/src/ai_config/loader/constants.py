"""
Constants for the loader module.

Author: TECHAKKENA
"""

from typing import Final

DEFAULT_ENCODING: Final[str] = "utf-8"

ENV_EXTENSION: Final[str] = ".env"

JSON_EXTENSION: Final[str] = ".json"

YAML_EXTENSIONS: Final[tuple[str, str]] = (
    ".yaml",
    ".yml",
)

TOML_EXTENSION: Final[str] = ".toml"

SUPPORTED_EXTENSIONS: Final[tuple[str, ...]] = (
    ENV_EXTENSION,
    JSON_EXTENSION,
    *YAML_EXTENSIONS,
    TOML_EXTENSION,
)

DEFAULT_CACHE_SIZE: Final[int] = 128
