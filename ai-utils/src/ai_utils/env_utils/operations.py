"""
Environment variable operations for the AI Engineering Framework.

This module provides helper functions for loading, retrieving,
setting, and removing environment variables.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

from ai_utils.env_utils.constants import DEFAULT_ENV_FILE
from ai_utils.env_utils.exceptions import (
    EnvironmentVariableError,
    EnvUtilsError,
)

__all__ = [
    "get_env",
    "get_required_env",
    "has_env",
    "load_env",
    "remove_env",
    "set_env",
]


def load_env(env_file: str | Path = DEFAULT_ENV_FILE) -> bool:
    """
    Load environment variables from a .env file.

    Parameters
    ----------
    env_file
        Path to the environment file.

    Returns
    -------
    bool
        True if the file was loaded successfully.
    """
    try:
        return load_dotenv(dotenv_path=env_file)
    except Exception as exc:
        raise EnvUtilsError(f"Unable to load environment file '{env_file}'.") from exc


def get_env(
    key: str,
    default: str | None = None,
) -> str | None:
    """
    Get an environment variable.
    """
    return os.getenv(key, default)


def get_required_env(key: str) -> str:
    """
    Get a required environment variable.

    Raises
    ------
    EnvironmentVariableError
        If the variable does not exist.
    """
    value = os.getenv(key)

    if value is None:
        raise EnvironmentVariableError(
            f"Required environment variable '{key}' is missing."
        )

    return value


def set_env(
    key: str,
    value: str,
) -> None:
    """
    Set an environment variable.
    """
    os.environ[key] = value


def has_env(key: str) -> bool:
    """
    Return True if an environment variable exists.
    """
    return key in os.environ


def remove_env(key: str) -> None:
    """
    Remove an environment variable if it exists.
    """
    os.environ.pop(key, None)
