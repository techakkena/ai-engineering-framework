from pathlib import Path

from .backup_manager import BackupManager
from .storage_manager import StorageManager


def main():

    storage = StorageManager()

    source = Path("storage/temp/sample.txt")

    storage.save(
        source,
        "Backup Test",
    )

    backup = BackupManager()

    backup_file = backup.backup(
        source,
    )

    print()

    print("Backup")
    print("----------------")

    print(backup_file)

    print()

    print("Exists")
    print("----------------")

    print(
        backup.exists(
            backup_file,
        )
    )

    print()

    print("Available Backups")
    print("----------------")

    print(
        backup.list_backups()
    )

    print()

    restored = Path(
        "storage/temp/restored.txt"
    )

    backup.restore(
        backup_file,
        restored,
    )

    print()

    print("Restore")
    print("----------------")

    print(
        storage.load(
            restored,
        )
    )

    print()

    backup.delete_backup(
        backup_file,
    )

    print("Backup Exists")

    print("----------------")

    print(
        backup.exists(
            backup_file,
        )
    )


if __name__ == "__main__":
    main()