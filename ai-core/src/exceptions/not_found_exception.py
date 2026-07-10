"""
AI Engineering Framework
Not Found Exception

Author : TECHAKKENA
"""

from typing import Any

from .base_exception import FrameworkException
from .error_codes import ErrorCode


class NotFoundException(FrameworkException):
    """
    Exception raised when a requested resource is not found.
    """

    def __init__(
        self,
        message: str = "Requested resource not found.",
        details: Any = None,
    ):

        super().__init__(
            message=message,
            error_code=ErrorCode.NOT_FOUND_ERROR.value,
            status_code=404,
            module="Not Found",
            details=details,
        )
