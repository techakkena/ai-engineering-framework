"""
AI Engineering Framework
Authentication Exception

Author : TECHAKKENA
"""

from typing import Any

from .base_exception import FrameworkException
from .error_codes import ErrorCode


class AuthenticationException(FrameworkException):
    """
    Exception raised for authentication failures.
    """

    def __init__(
        self,
        message: str = "Authentication failed.",
        details: Any = None,
    ):

        super().__init__(
            message=message,
            error_code=ErrorCode.AUTHENTICATION_ERROR.value,
            status_code=401,
            module="Authentication",
            details=details,
        )
