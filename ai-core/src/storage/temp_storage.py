"""
AI Engineering Framework
Temporary Storage

Author : TECHAKKENA
"""

from pathlib import Path
from uuid import uuid4
from typing import Union

from config.settings import settings

from .storage_manager import StorageManager


class TempStorage:
    """
    Temporary file storage.
    """

    def __init__(self):

        self.storage = StorageManager()

        self.temp_dir = settings.TEMP_FOLDER

    def create(
        self,
        suffix: str,
        data: Union[str, bytes],
    ) -> Path:
        """
        Create a temporary file.
        """

        filename = f"{uuid4()}{suffix}"

        file_path = self.temp_dir / filename

        self.storage.save(
            file_path,
            data,
        )

        return file_path

    def read(
        self,
        file_path: Path,
    ):

        return self.storage.load(file_path)

    def delete(
        self,
        file_path: Path,
    ) -> bool:

        return self.storage.delete(file_path)

    def exists(
        self,
        file_path: Path,
    ) -> bool:

        return self.storage.exists(file_path)

    def clear(self):
        """
        Delete every temporary file.
        """

        for file in self.storage.list_files(
            self.temp_dir
        ):
            self.storage.delete(file)