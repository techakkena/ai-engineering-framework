from exceptions.file_exception import FileException


def test_file_exception():
    message = "File operation failed."
    details = {"info": "Additional file error details"}

    exception = FileException(message=message, details=details)

    assert exception.message == message
    assert exception.error_code == "FILE001"
    assert exception.status_code == 400
    assert exception.module == "File"
    assert exception.details == details