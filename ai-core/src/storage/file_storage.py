"""
AI Engineering Framework
File Storage 

Author : TECHAKKENA
"""

from pathlib import Path
from typing import Union

from .storage_provider import StorageProvider
from exceptions.file_exception import FileException


class FileStorage(StorageProvider):
    """
    Local filesystem storage implementation.
    """

    def save(
        self,
        file_path: Path,
        data: Union[str, bytes],
    ) -> bool:
        """
        Save data to a file.
        """

        try:

            file_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            if isinstance(data, bytes):

                file_path.write_bytes(data)

            else:

                file_path.write_text(
                    data,
                    encoding="utf-8",
                )

            return True

        except Exception as exc:

            raise FileException(
                message="Unable to save file.",
                details={
                    "file": str(file_path),
                    "error": str(exc),
                },
            )

    def load(
        self,
        file_path: Path,
    ) -> Union[str, bytes]:
        """
        Load file contents.
        """

        if not file_path.exists():

            raise FileException(
                message="File not found.",
                details={
                    "file": str(file_path),
                },
            )

        return file_path.read_text(
            encoding="utf-8",
        )

    def delete(
        self,
        file_path: Path,
    ) -> bool:
        """
        Delete file.
        """

        if file_path.exists():

            file_path.unlink()

        return True

    def exists(
        self,
        file_path: Path,
    ) -> bool:

        return file_path.exists()

    def list_files(
        self,
        directory: Path,
    ):

        if not directory.exists():

            return []

        return sorted(
            [
                file
                for file in directory.iterdir()
                if file.is_file()
            ]
    )

    def size(
        self,
        file_path: Path,
    ) -> int:

        if not file_path.exists():

            return 0

        return file_path.stat().st_size

    