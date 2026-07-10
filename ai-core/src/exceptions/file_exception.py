"""
AI Engineering Framework
File Exception

Author : TECHAKKENA
"""

from typing import Any

from .base_exception import FrameworkException
from .error_codes import ErrorCode


class FileException(FrameworkException):
    """
    Exception raised for file-related errors.
    """

    def __init__(
        self,
        message: str = "File operation failed.",
        details: Any = None,
    ):

        super().__init__(
            message=message,
            error_code=ErrorCode.FILE_ERROR.value,
            status_code=400,
            module="File",
            details=details,
        )
