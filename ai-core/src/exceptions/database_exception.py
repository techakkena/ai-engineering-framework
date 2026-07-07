"""
AI Engineering Framework
Database Exception

Author : TECHAKKENA
"""

from typing import Any

from .base_exception import FrameworkException
from .error_codes import ErrorCode


class DatabaseException(FrameworkException):
    """
    Exception raised for database-related failures.
    """

    def __init__(
        self,
        message: str = "Database operation failed.",
        details: Any = None,
    ):

        super().__init__(
            message=message,
            error_code=ErrorCode.DATABASE_ERROR.value,
            status_code=500,
            module="Database",
            details=details,
        )