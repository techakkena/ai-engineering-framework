from exceptions.not_found_exception import NotFoundException
from exceptions.error_codes import ErrorCode

def test_not_found_exception():
    message = "Resource not found."
    details = {"info": "Additional not found error details"}

    exception = NotFoundException(message=message, details=details)

    assert exception.message == message
    assert exception.error_code == ErrorCode.NOT_FOUND_ERROR.value
    assert exception.status_code == 404
    assert exception.module == "Not Found"
    assert exception.details == details

