"""
AI Engineering Framework
JSON Utilities

Author : TECHAKKENA
"""

import json
from pathlib import Path
from typing import Any

from .path_utils import PathUtils


class JsonUtils:
    """
    Utility methods for JSON operations.
    """

    @staticmethod
    def dumps(
        data: Any,
        indent: int = 4,
    ) -> str:
        """
        Convert Python object to JSON string.
        """
        return json.dumps(
            data,
            indent=indent,
            ensure_ascii=False,
        )

    @staticmethod
    def loads(
        data: str,
    ) -> Any:
        """
        Convert JSON string to Python object.
        """
        return json.loads(data)

    @staticmethod
    def write(
        file_path: Path,
        data: Any,
    ) -> None:
        """
        Write JSON to file.
        """

        PathUtils.ensure_directory(file_path)

        file_path.write_text(
            JsonUtils.dumps(data),
            encoding="utf-8",
        )

    @staticmethod
    def read(
        file_path: Path,
    ) -> Any:
        """
        Read JSON from file.
        """

        return JsonUtils.loads(
            file_path.read_text(
                encoding="utf-8",
            )
        )

    @staticmethod
    def pretty_print(
        data: Any,
    ) -> None:
        """
        Print formatted JSON.
        """

        print(
            JsonUtils.dumps(data)
        )