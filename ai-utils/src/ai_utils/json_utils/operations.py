"""
JSON operations for the AI Engineering Framework.

This module provides helper functions for reading, writing,
serializing, and validating JSON data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ai_utils.json_utils.constants import (
    DEFAULT_ENCODING,
    DEFAULT_ENSURE_ASCII,
    DEFAULT_INDENT,
    DEFAULT_SORT_KEYS,
)
from ai_utils.json_utils.exceptions import (
    JsonDecodeError,
    JsonReadError,
    JsonWriteError,
)

__all__ = [
    "dumps",
    "is_valid_json",
    "loads",
    "read_json",
    "write_json",
]


def read_json(file_path: str | Path) -> dict[str, Any]:
    """
    Read JSON data from a file.

    Parameters
    ----------
    file_path
        Path to the JSON file.

    Returns
    -------
    dict[str, Any]
        Parsed JSON object.
    """
    try:
        path = Path(file_path)

        with path.open("r", encoding=DEFAULT_ENCODING) as file:
            data: dict[str, Any] = json.load(file)

        return data

    except json.JSONDecodeError as exc:
        raise JsonDecodeError(f"Invalid JSON in '{file_path}'.") from exc

    except Exception as exc:
        raise JsonReadError(f"Unable to read JSON file '{file_path}'.") from exc


def write_json(
    file_path: str | Path,
    data: dict[str, Any],
) -> None:
    """
    Write JSON data to a file.
    """
    try:
        path = Path(file_path)

        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", encoding=DEFAULT_ENCODING) as file:
            json.dump(
                data,
                file,
                indent=DEFAULT_INDENT,
                ensure_ascii=DEFAULT_ENSURE_ASCII,
                sort_keys=DEFAULT_SORT_KEYS,
            )

    except Exception as exc:
        raise JsonWriteError(f"Unable to write JSON file '{file_path}'.") from exc


def loads(json_string: str) -> dict[str, Any]:
    """
    Deserialize a JSON string.
    """
    try:
        data: dict[str, Any] = json.loads(json_string)
        return data

    except json.JSONDecodeError as exc:
        raise JsonDecodeError("Invalid JSON string.") from exc


def dumps(data: dict[str, Any]) -> str:
    """
    Serialize a dictionary to a JSON string.
    """
    return json.dumps(
        data,
        indent=DEFAULT_INDENT,
        ensure_ascii=DEFAULT_ENSURE_ASCII,
        sort_keys=DEFAULT_SORT_KEYS,
    )


def is_valid_json(json_string: str) -> bool:
    """
    Return True if the string contains valid JSON.
    """
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False
