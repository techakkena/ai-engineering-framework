from __future__ import annotations

from exceptions.error_codes import ErrorCode
from exceptions.integration_exception import IntegrationException


def test_integration_exception():
    message = "Integration error occurred."
    details = {"info": "Additional integration error details"}

    exception = IntegrationException(message=message, details=details)

    assert exception.message == message
    assert exception.error_code == ErrorCode.INTEGRATION_ERROR.value
    assert exception.status_code == 502
    assert exception.module == "Integration"
    assert exception.details == details
