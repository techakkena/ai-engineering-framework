"""
AI Engineering Framework
Integration Exception

Author : TECHAKKENA
"""

from typing import Any

from .base_exception import FrameworkException
from .error_codes import ErrorCode


class IntegrationException(FrameworkException):
    """
    Exception raised for third-party integration failures.
    """

    def __init__(
        self,
        message: str = "Integration failed.",
        details: Any = None,
    ):

        super().__init__(
            message=message,
            error_code=ErrorCode.INTEGRATION_ERROR.value,
            status_code=502,
            module="Integration",
            details=details,
        ) 