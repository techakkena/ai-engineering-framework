"""
File operations for the file utilities package.
"""

from __future__ import annotations

from pathlib import Path

from ai_utils.file_utils.constants import DEFAULT_ENCODING
from ai_utils.file_utils.exceptions import (
    FileReadError,
    FileWriteError,
)

__all__ = [
    "append_text",
    "file_exists",
    "read_bytes",
    "read_text",
    "write_bytes",
    "write_text",
]


def read_text(
    file_path: str | Path,
    encoding: str = DEFAULT_ENCODING,
) -> str:
    """Read text from a file."""
    try:
        path = Path(file_path)
        return path.read_text(encoding=encoding)
    except Exception as exc:
        raise FileReadError(f"Failed to read '{file_path}'.") from exc


def write_text(
    file_path: str | Path,
    content: str,
    encoding: str = DEFAULT_ENCODING,
) -> None:
    """Write text to a file."""
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding=encoding)
    except Exception as exc:
        raise FileWriteError(f"Failed to write '{file_path}'.") from exc


def append_text(
    file_path: str | Path,
    content: str,
    encoding: str = DEFAULT_ENCODING,
) -> None:
    """Append text to a file."""
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("a", encoding=encoding) as file:
            file.write(content)

    except Exception as exc:
        raise FileWriteError(f"Failed to append '{file_path}'.") from exc


def read_bytes(
    file_path: str | Path,
) -> bytes:
    """Read bytes from a file."""
    try:
        path = Path(file_path)
        return path.read_bytes()
    except Exception as exc:
        raise FileReadError(f"Failed to read '{file_path}'.") from exc


def write_bytes(
    file_path: str | Path,
    content: bytes,
) -> None:
    """Write bytes to a file."""
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    except Exception as exc:
        raise FileWriteError(f"Failed to write '{file_path}'.") from exc


def file_exists(
    file_path: str | Path,
) -> bool:
    """Return True if the file exists."""
    try:
        path = Path(file_path)
        return path.is_file()
    except Exception:
        return False
