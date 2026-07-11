"""
Constants for the file utilities package.

This module defines the default values used throughout the
file utilities package.
"""

from __future__ import annotations

__all__ = [
    "DEFAULT_ENCODING",
    "DEFAULT_BUFFER_SIZE",
    "DEFAULT_CHUNK_SIZE",
    "DEFAULT_NEWLINE",
]

# ---------------------------------------------------------------------
# Encoding
# ---------------------------------------------------------------------

DEFAULT_ENCODING: str = "utf-8"

# ---------------------------------------------------------------------
# File I/O
# ---------------------------------------------------------------------

DEFAULT_BUFFER_SIZE: int = 8192

DEFAULT_CHUNK_SIZE: int = 64 * 1024

DEFAULT_NEWLINE: str = "\n"
