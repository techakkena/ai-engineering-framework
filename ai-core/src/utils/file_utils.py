"""
AI Engineering Framework
File Utilities

Author : TECHAKKENA
"""

import shutil
from pathlib import Path


class FileUtils:
    """
    Utility methods for file operations.
    """

    @staticmethod
    def read_text(
        file_path: Path,
        encoding: str = "utf-8",
    ) -> str:

        return file_path.read_text(
            encoding=encoding,
        )

    @staticmethod
    def write_text(
        file_path: Path,
        data: str,
        encoding: str = "utf-8",
    ):

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path.write_text(
            data,
            encoding=encoding,
        )

    @staticmethod
    def copy(
        source: Path,
        destination: Path,
    ):

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        shutil.copy2(
            source,
            destination,
        )

    @staticmethod
    def move(
        source: Path,
        destination: Path,
    ):

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        shutil.move(
            source,
            destination,
        )

    @staticmethod
    def rename(
        source: Path,
        new_name: str,
    ) -> Path:

        destination = source.with_name(
            new_name,
        )

        source.rename(destination)

        return destination

    @staticmethod
    def size(
        file_path: Path,
    ) -> int:

        return file_path.stat().st_size

    @staticmethod
    def delete(
        file_path: Path,
    ) -> bool:

        if file_path.exists():

            file_path.unlink()

            return True

        return False