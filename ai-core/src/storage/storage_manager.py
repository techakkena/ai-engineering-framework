"""
AI Engineering Framework
Storage Manager

Author : TECHAKKENA
"""

from pathlib import Path
from typing import Union

from constants.storage_constants import StorageTypes

from .storage_factory import StorageFactory
from .storage_provider import StorageProvider


class StorageManager:
    """
    High-level storage manager.

    Delegates storage operations to the
    configured storage provider.
    """

    def __init__(
        self,
        provider: StorageProvider | None = None,
    ):

        self.provider = provider or StorageFactory.create(StorageTypes.LOCAL)

    def save(
        self,
        file_path: Path,
        data: Union[str, bytes],
    ) -> bool:

        return self.provider.save(
            file_path,
            data,
        )

    def load(
        self,
        file_path: Path,
    ):

        return self.provider.load(file_path)

    def delete(
        self,
        file_path: Path,
    ) -> bool:

        return self.provider.delete(file_path)

    def exists(
        self,
        file_path: Path,
    ) -> bool:

        return self.provider.exists(file_path)

    def list_files(
        self,
        directory: Path,
    ):

        return self.provider.list_files(directory)

    def size(
        self,
        file_path: Path,
    ) -> int:

        return self.provider.size(file_path)
