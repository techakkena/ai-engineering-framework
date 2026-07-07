"""
AI Engineering Framework
Network Exception

Author : TECHAKKENA
"""

from typing import Any

from .base_exception import FrameworkException
from .error_codes import ErrorCode


class NetworkException(FrameworkException):
    """
    Exception raised for network-related errors.
    """

    def __init__(
        self,
        message: str = "Network operation failed.",
        details: Any = None,
    ):

        super().__init__(
            message=message,
            error_code=ErrorCode.NETWORK_ERROR.value,
            status_code=503,
            module="Network",
            details=details,
        )