"""
AI Engineering Framework
Backup Manager

Author : TECHAKKENA
"""

import shutil
from pathlib import Path

from config.settings import settings

from .storage_manager import StorageManager


class BackupManager:
    """
    Handles backup and restore operations.
    """

    def __init__(self):

        self.storage = StorageManager()

        self.backup_dir = settings.BACKUP_FOLDER

    def backup(
        self,
        source: Path,
    ) -> Path:
        """
        Create a backup of a file.
        """

        destination = self.backup_dir / source.name

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        shutil.copy2(
            source,
            destination,
        )

        return destination

    def restore(
        self,
        backup_file: Path,
        destination: Path,
    ) -> Path:
        """
        Restore a backup.
        """

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        shutil.copy2(
            backup_file,
            destination,
        )

        return destination

    def delete_backup(
        self,
        backup_file: Path,
    ) -> bool:
        """
        Delete a backup file.
        """

        return self.storage.delete(
            backup_file,
        )

    def exists(
        self,
        backup_file: Path,
    ) -> bool:
        """
        Check backup existence.
        """

        return self.storage.exists(
            backup_file,
        )

    def list_backups(self):
        """
        List all backups.
        """

        return self.storage.list_files(
            self.backup_dir,
        )