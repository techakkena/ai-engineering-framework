from exceptions.base_exception import FrameworkException
from exceptions.error_codes import ErrorCode

def test_framework_exception():
    message = "An unexpected error occurred."
    details = {"info": "Additional error details"}

    exception = FrameworkException(message=message, details=details)

    assert exception.message == message
    assert exception.error_code == "BASE001"
    assert exception.status_code == 500
    assert exception.module == "Framework"
    assert exception.details == details

def test_framework_exception_to_dict():
    message = "An unexpected error occurred."
    details = {"info": "Additional error details"}

    exception = FrameworkException(message=message, details=details)
    exception_dict = exception.to_dict()

    assert exception_dict["message"] == message
    assert exception_dict["error_code"] == "BASE001"
    assert exception_dict["status_code"] == 500
    assert exception_dict["module"] == "Framework"
    assert exception_dict["details"] == details
    assert "timestamp" in exception_dict

def test_framework_exception_str():
    message = "An unexpected error occurred."
    details = {"info": "Additional error details"}

    exception = FrameworkException(message=message, details=details)
    exception_str = str(exception)

    assert exception_str == f"[{exception.error_code}] {message}"
