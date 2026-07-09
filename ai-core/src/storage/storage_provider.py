"""
AI Engineering Framework
Storage Provider

Author : TECHAKKENA
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union

class StorageProvider(ABC):
    """
    Abstract base class for all storage providers.

    Every storage backend (local filesystem, cloud,
    object storage, vector storage, etc.) should
    implement this interface.
    """
 
    @abstractmethod
    def save(
        self,
        file_path: Path,
        data: Union[str, bytes],
    ) -> bool:
        """
        Save data to storage.
        """
        pass

    @abstractmethod
    def load(
        self,
        file_path: Path,
    ) -> Union[str, bytes]:
        """
        Load data from storage.
        """
        pass

    @abstractmethod
    def delete(self, file_path: Path) -> bool:
        """
        Delete a file from storage.
        """
        pass

    @abstractmethod
    def exists(self, file_path: Path) -> bool:
        """
        Check whether a file exists.
        """
        pass

    @abstractmethod
    def list_files(self, directory: Path):
        """
        Return all files in a directory.
        """
        pass

    @abstractmethod
    def size(self, file_path: Path) -> int:
        """
        Return file size in bytes.
        """
        pass