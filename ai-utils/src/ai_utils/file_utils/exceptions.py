"""
Custom exceptions for the file utilities package.

This module defines the exception hierarchy used by the file utilities
package. These exceptions provide clear and consistent error reporting
for file and directory operations throughout the AI Engineering Framework.
"""

from __future__ import annotations

__all__ = [
    "FileUtilsError",
    "FileReadError",
    "FileWriteError",
    "FileOperationError",
    "DirectoryCreationError",
]


class FileUtilsError(Exception):
    """Base exception for all file utility errors."""


class FileReadError(FileUtilsError):
    """Raised when a file cannot be read."""


class FileWriteError(FileUtilsError):
    """Raised when a file cannot be written."""


class FileOperationError(FileUtilsError):
    """Raised when a generic file operation fails."""


class DirectoryCreationError(FileUtilsError):
    """Raised when a directory cannot be created."""
