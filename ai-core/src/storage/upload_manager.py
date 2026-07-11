"""
AI Engineering Framework
Upload Manager

Author : TECHAKKENA
"""

from pathlib import Path
from typing import Union
from uuid import uuid4

from config.settings import settings

from .storage_manager import StorageManager


class UploadManager:
    """
    Handles upload operations.
    """

    def __init__(self):

        self.storage = StorageManager()

    def upload(
        self,
        filename: str,
        data: Union[str, bytes],
    ) -> Path:
        """
        Upload a file.
        """

        file_path = settings.UPLOAD_FOLDER / f"{uuid4()}_{filename}"

        self.storage.save(
            file_path,
            data,
        )

        return file_path

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

    def size(
        self,
        file_path: Path,
    ) -> int:

        return self.storage.size(file_path)
