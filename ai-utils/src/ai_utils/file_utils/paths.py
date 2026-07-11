"""
Path utilities for the file utilities package.
"""

from __future__ import annotations

from pathlib import Path

from ai_utils.file_utils.exceptions import DirectoryCreationError

__all__ = [
    "ensure_directory",
    "get_extension",
    "get_filename",
    "get_stem",
    "resolve_path",
]


def ensure_directory(directory: str | Path) -> Path:
    """
    Create a directory if it does not exist.

    Returns
    -------
    Path
        The resolved directory path.
    """
    try:
        path = Path(directory)
        path.mkdir(parents=True, exist_ok=True)
        return path
    except Exception as exc:
        raise DirectoryCreationError(
            f"Failed to create directory '{directory}'."
        ) from exc


def resolve_path(path: str | Path) -> Path:
    """Return the absolute resolved path."""
    return Path(path).expanduser().resolve()


def get_filename(path: str | Path) -> str:
    """Return the filename including extension."""
    return Path(path).name


def get_stem(path: str | Path) -> str:
    """Return the filename without extension."""
    return Path(path).stem


def get_extension(path: str | Path) -> str:
    """Return the file extension."""
    return Path(path).suffix
