from exceptions.authorization_exception import AuthorizationException
from exceptions.error_codes import ErrorCode


def test_authorization_exception():
    message = "User does not have permission to access this resource."
    details = {"user_id": 123, "resource": "admin_panel"}

    exception = AuthorizationException(message=message, details=details)

    assert exception.message == message
    assert exception.error_code == ErrorCode.AUTHORIZATION_ERROR.value
    assert exception.status_code == 403
    assert exception.module == "Authorization"
    assert exception.details == details

