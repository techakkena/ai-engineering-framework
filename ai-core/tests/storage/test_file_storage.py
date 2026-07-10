from pathlib import Path

from storage.file_storage import FileStorage


def test_save():
    storage = FileStorage()

    file_path = Path("test_file.txt")
    data = "Hello, World!"

    result = storage.save(file_path, data)

    assert result is True
    assert file_path.exists()

    # Clean up
    file_path.unlink()


def test_load():
    storage = FileStorage()

    file_path = Path("test_file.txt")
    data = "Hello, World!"

    # Save the file first
    storage.save(file_path, data)

    loaded_data = storage.load(file_path)

    assert loaded_data == data

    # Clean up
    file_path.unlink()


def test_delete():
    storage = FileStorage()

    file_path = Path("test_file.txt")
    data = "Hello, World!"

    # Save the file first
    storage.save(file_path, data)

    # Delete the file
    file_path.unlink()

    assert not file_path.exists()


def test_exists():
    storage = FileStorage()

    file_path = Path("test_file.txt")
    data = "Hello, World!"

    # Save the file first
    storage.save(file_path, data)

    assert storage.exists(file_path) is True

    # Clean up
    file_path.unlink()

    assert storage.exists(file_path) is False


def test_list_files():
    storage = FileStorage()

    # Create test files
    file1 = Path("test_file1.txt")
    file2 = Path("test_file2.txt")
    data = "Hello, World!"

    storage.save(file1, data)
    storage.save(file2, data)

    files = storage.list_files(Path("."))

    assert file1 in files
    assert file2 in files

    # Clean up
    file1.unlink()
    file2.unlink()


def test_size():
    storage = FileStorage()

    file_path = Path("test_file.txt")
    data = "Hello, World!"

    # Save the file first
    storage.save(file_path, data)

    size = storage.size(file_path)

    assert size == len(data.encode("utf-8"))

    # Clean up
    file_path.unlink()
