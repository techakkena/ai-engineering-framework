from __future__ import annotations

from exceptions.authentication_exception import AuthenticationException
from exceptions.error_codes import ErrorCode


def test_authentication_exception():
    message = "Invalid username or password."
    details = {"username": "admin", "reason": "Invalid credentials"}

    exception = AuthenticationException(message=message, details=details)

    assert exception.message == message
    assert exception.error_code == ErrorCode.AUTHENTICATION_ERROR.value
    assert exception.status_code == 401
    assert exception.module == "Authentication"
    assert exception.details == details
