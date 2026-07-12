"""
Environment loading operations.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Dict

from dotenv import load_dotenv

from ai_config.environment.constants import (
    DEFAULT_ENCODING,
    DEFAULT_ENV_FILE,
)
from ai_config.environment.exceptions import (
    EnvironmentVariableNotFoundError,
)


class EnvironmentLoader:
    """
    Loads and provides access to environment variables.
    """

    def __init__(
        self,
        env_file: str | Path = DEFAULT_ENV_FILE,
        encoding: str = DEFAULT_ENCODING,
    ) -> None:
        self._env_file = Path(env_file)
        self._encoding = encoding

        self.load()

    def load(self) -> None:
        """
        Load environment variables from a .env file.
        """
        load_dotenv(
            dotenv_path=self._env_file,
            override=False,
            encoding=self._encoding,
        )

    def reload(self) -> None:
        """
        Reload environment variables.
        """
        load_dotenv(
            dotenv_path=self._env_file,
            override=True,
            encoding=self._encoding,
        )

    def get(
        self,
        key: str,
        default: str | None = None,
    ) -> str | None:
        """
        Retrieve an environment variable.
        """
        return os.getenv(key, default)

    def require(self, key: str) -> str:
        """
        Retrieve a required environment variable.

        Raises:
            EnvironmentVariableNotFoundError
        """
        value = os.getenv(key)

        if value is None:
            raise EnvironmentVariableNotFoundError(
                f"Environment variable '{key}' not found."
            )

        return value

    def exists(self, key: str) -> bool:
        """
        Check whether an environment variable exists.
        """
        return key in os.environ

    def all(self) -> Dict[str, str]:
        """
        Return all environment variables.
        """
        return dict(os.environ)
