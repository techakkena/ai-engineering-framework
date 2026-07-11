"""
Hashing utilities for the file utilities package.

This module provides helper functions for calculating file hashes.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

from ai_utils.file_utils.constants import DEFAULT_CHUNK_SIZE
from ai_utils.file_utils.exceptions import FileReadError

__all__ = [
    "calculate_hash",
    "md5",
    "sha256",
]


def calculate_hash(
    file_path: str | Path,
    algorithm: str = "sha256",
) -> str:
    """
    Calculate the hash of a file.

    Parameters
    ----------
    file_path
        Path to the file.

    algorithm
        Hash algorithm (sha256 or md5).

    Returns
    -------
    str
        Hexadecimal hash string.
    """
    try:
        path = Path(file_path)

        hasher = hashlib.new(algorithm)

        with path.open("rb") as file:
            while chunk := file.read(DEFAULT_CHUNK_SIZE):
                hasher.update(chunk)

        return hasher.hexdigest()

    except Exception as exc:
        raise FileReadError(
            f"Unable to calculate {algorithm} hash for '{file_path}'."
        ) from exc


def sha256(
    file_path: str | Path,
) -> str:
    """
    Calculate the SHA-256 hash of a file.
    """
    return calculate_hash(file_path, "sha256")


def md5(
    file_path: str | Path,
) -> str:
    """
    Calculate the MD5 hash of a file.
    """
    return calculate_hash(file_path, "md5")
