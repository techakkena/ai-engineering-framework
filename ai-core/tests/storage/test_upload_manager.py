from storage.upload_manager import UploadManager


def test_upload_manager_upload_delete_exists():
    upload_manager = UploadManager()

    # Upload a file
    file_path = upload_manager.upload(
        filename="test.txt",
        data="Hello, World!",
    )

    assert upload_manager.exists(file_path) is True

    # Delete the uploaded file
    deleted = upload_manager.delete(file_path)
    assert deleted is True
    assert upload_manager.exists(file_path) is False
