"""
AI Engineering Framework
Path Utilities

Author : TECHAKKENA
"""

import shutil
from pathlib import Path


class PathUtils:
    """
    Utility methods for filesystem paths.
    """

    @staticmethod
    def exists(path: Path) -> bool:
        """
        Check whether a path exists.
        """
        return path.exists()

    @staticmethod
    def create_directory(path: Path) -> Path:
        """
        Create a directory.
        """
        path.mkdir(
            parents=True,
            exist_ok=True,
        )
        return path

    @staticmethod
    def ensure_directory(path: Path) -> Path:
        """
        Ensure parent directory exists.
        """
        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        return path

    @staticmethod
    def delete(path: Path) -> bool:
        """
        Delete a file or directory.
        """
        if not path.exists():
            return False

        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()

        return True

    @staticmethod
    def file_name(path: Path) -> str:
        """
        Return file name.
        """
        return path.name

    @staticmethod
    def extension(path: Path) -> str:
        """
        Return file extension.
        """
        return path.suffix

    @staticmethod
    def parent(path: Path) -> Path:
        """
        Return parent directory.
        """
        return path.parent

    @staticmethod
    def resolve(path: Path) -> Path:
        """
        Return absolute path.
        """
        return path.resolve()

    @staticmethod
    def join(*parts) -> Path:
        """
        Join path parts.
        """
        return Path(*parts)