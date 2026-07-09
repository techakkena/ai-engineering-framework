from pathlib import Path
from storage.storage_manager import StorageManager


def test_initialize_storage_manager():
    storage_manager = StorageManager()

    assert isinstance(storage_manager, StorageManager)
    assert storage_manager.provider is not None

def test_save():
    storage_manager = StorageManager()

    file_path = Path("test_file.txt")
    data = "Hello, World!"

    result = storage_manager.save(file_path, data)

    assert result is True
    assert file_path.exists()

    # Clean up
    file_path.unlink()

def test_load():
    storage_manager = StorageManager()

    file_path = Path("test_file.txt")
    data = "Hello, World!"

    # Save the file first
    storage_manager.save(file_path, data)

    loaded_data = storage_manager.load(file_path)

    assert loaded_data == data

    # Clean up
    file_path.unlink()

def test_delete():
    storage_manager = StorageManager()

    file_path = Path("test_file.txt")
    data = "Hello, World!"

    # Save the file first
    storage_manager.save(file_path, data)

    # Delete the file
    storage_manager.delete(file_path)

    assert not file_path.exists()

def test_exists():
    storage_manager = StorageManager()

    file_path = Path("test_file.txt")
    data = "Hello, World!"

    # Save the file first
    storage_manager.save(file_path, data)

    assert storage_manager.exists(file_path) is True

    # Clean up
    file_path.unlink()

def test_list_files():
    storage_manager = StorageManager()

    directory = Path("test_directory")
    directory.mkdir(exist_ok=True)

    file1 = directory / "file1.txt"
    file2 = directory / "file2.txt"

    storage_manager.save(file1, "File 1 content")
    storage_manager.save(file2, "File 2 content")

    files = storage_manager.list_files(directory)

    assert len(files) == 2
    assert file1 in files
    assert file2 in files

    # Clean up
    file1.unlink()
    file2.unlink()
    directory.rmdir()

def test_size():
    storage_manager = StorageManager()

    file_path = Path("test_file.txt")
    data = "Hello, World!"

    # Save the file first
    storage_manager.save(file_path, data)

    size = file_path.stat().st_size

    assert size == len(data)

    # Clean up
    file_path.unlink()