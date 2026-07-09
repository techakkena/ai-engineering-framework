from exceptions.validation_exception import ValidationException
from exceptions.error_codes import ErrorCode

def test_validation_exception():
    message = "Validation failed."
    details = {"info": "Additional validation error details"}

    exception = ValidationException(message=message, details=details)

    assert exception.message == message
    assert exception.error_code == ErrorCode.VALIDATION_ERROR.value
    assert exception.status_code == 400
    assert exception.module == "Validation"
    assert exception.details == details
