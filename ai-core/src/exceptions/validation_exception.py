"""
AI Engineering Framework
Validation Exception

Author : TECHAKKENA
"""

from typing import Any

from .base_exception import FrameworkException
from .error_codes import ErrorCode


class ValidationException(FrameworkException):
    """
    Exception raised for validation errors.
    """

    def __init__(
        self,
        message: str = "Validation failed.",
        details: Any = None,
    ):

        super().__init__(
            message=message,
            error_code=ErrorCode.VALIDATION_ERROR.value,
            status_code=400,
            module="Validation",
            details=details,
        )
