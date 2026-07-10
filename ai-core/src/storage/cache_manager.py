"""
AI Engineering Framework
Cache Manager

Author : TECHAKKENA
"""

import json
from pathlib import Path
from typing import Any

from config.settings import settings

from .storage_manager import StorageManager


class CacheManager:
    """
    File-based cache manager.
    """

    def __init__(self):

        self.storage = StorageManager()

        self.cache_dir = settings.CACHE_FOLDER

    def _cache_file(self, key: str) -> Path:
        """
        Return cache file path.
        """

        return self.cache_dir / f"{key}.json"

    def set(
        self,
        key: str,
        value: Any,
    ) -> bool:
        """
        Save value to cache.
        """

        file_path = self._cache_file(key)

        data = json.dumps(
            value,
            indent=4,
        )

        return self.storage.save(
            file_path,
            data,
        )

    def get(
        self,
        key: str,
    ) -> Any:
        """
        Load cached value.
        """

        file_path = self._cache_file(key)

        if not self.storage.exists(file_path):
            return None

        data = self.storage.load(file_path)

        return json.loads(data)

    def exists(
        self,
        key: str,
    ) -> bool:

        return self.storage.exists(self._cache_file(key))

    def delete(
        self,
        key: str,
    ) -> bool:

        return self.storage.delete(self._cache_file(key))

    def clear(self):
        """
        Remove all cache files.
        """

        for file in self.storage.list_files(self.cache_dir):
            self.storage.delete(file)
