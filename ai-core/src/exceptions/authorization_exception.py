"""
AI Engineering Framework
Authorization Exception

Author : TECHAKKENA
"""

from typing import Any

from .base_exception import FrameworkException
from .error_codes import ErrorCode


class AuthorizationException(FrameworkException):
    """
    Exception raised for authorization failures.
    """

    def __init__(
        self,
        message: str = "Authorization failed.",
        details: Any = None,
    ):

        super().__init__(
            message=message,
            error_code=ErrorCode.AUTHORIZATION_ERROR.value,
            status_code=403,
            module="Authorization",
            details=details,
        )
