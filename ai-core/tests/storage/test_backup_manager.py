from pathlib import Path

from storage.backup_manager import BackupManager
from storage.storage_manager import StorageManager


def test_backup_manager_creation():
    backup_manager = BackupManager()

    assert backup_manager is not None
    assert isinstance(backup_manager.storage, StorageManager)
    assert isinstance(backup_manager.backup_dir, Path)


def test_backup():
    backup_manager = BackupManager()

    # Create a temporary file to backup
    temp_file = Path("temp_test_file.txt")
    temp_file.write_text("This is a test file.")

    backup_path = backup_manager.backup(temp_file)

    assert backup_path.exists()
    assert backup_path.read_text() == "This is a test file."

    # Clean up
    temp_file.unlink()
    backup_path.unlink()


def test_restore():
    backup_manager = BackupManager()

    # Create a temporary backup file
    backup_file = Path("temp_backup_file.txt")
    backup_file.write_text("This is a backup file.")

    restore_path = Path("restored_test_file.txt")
    restored_path = backup_manager.restore(backup_file, restore_path)

    assert restored_path.exists()
    assert restored_path.read_text() == "This is a backup file."

    # Clean up
    backup_file.unlink()
    restored_path.unlink()


def test_delete_backup():
    backup_manager = BackupManager()

    backup_file = Path("temp_backup_file.txt")
    backup_file.write_text("This is a backup file.")

    backup_manager.delete_backup(backup_file)

    assert not backup_file.exists()


def test_exists():
    backup_manager = BackupManager()

    # Create a temporary backup file
    backup_file = Path("temp_backup_file.txt")
    backup_file.write_text("This is a backup file.")

    assert backup_manager.exists(backup_file)

    # Clean up
    backup_file.unlink()


def test_list_backups(tmp_path):
    backup_manager = BackupManager()

    source1 = tmp_path / "file1.txt"
    source2 = tmp_path / "file2.txt"

    source1.write_text("File 1")
    source2.write_text("File 2")

    backup_manager.backup(source1)
    backup_manager.backup(source2)

    backups = backup_manager.list_backups()

    assert any(file.name == "file1.txt" for file in backups)
    assert any(file.name == "file2.txt" for file in backups)
