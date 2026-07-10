from exceptions.error_codes import ErrorCode
from exceptions.network_exception import NetworkException


def test_network_exception():
    message = "Network error occurred."
    details = {"info": "Additional network error details"}

    exception = NetworkException(message=message, details=details)

    assert exception.message == message
    assert exception.error_code == ErrorCode.NETWORK_ERROR.value
    assert exception.status_code == 503
    assert exception.module == "Network"
    assert exception.details == details
