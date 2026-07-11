from storage.temp_storage import TempStorage


def test_temp_storage_create_read_delete():
    temp_storage = TempStorage()

    # Create a temporary file
    file_path = temp_storage.create(
        suffix=".txt",
        data="Hello, World!",
    )

    assert temp_storage.exists(file_path) is True

    # Read the content of the temporary file
    content = temp_storage.read(file_path)
    assert content == "Hello, World!"

    # Delete the temporary file
    deleted = temp_storage.delete(file_path)
    assert deleted is True
    assert temp_storage.exists(file_path) is False
