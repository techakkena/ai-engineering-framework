"""
AI Engineering Framework
Configuration Exception

Author : TECHAKKENA
"""

from typing import Any

from .base_exception import FrameworkException
from .error_codes import ErrorCode


class ConfigurationException(FrameworkException):
    """
    Exception raised for configuration-related errors.
    """

    def __init__(
        self,
        message: str = "Configuration error.",
        details: Any = None,
    ):

        super().__init__(
            message=message,
            error_code=ErrorCode.CONFIGURATION_ERROR.value,
            status_code=500,
            module="Configuration",
            details=details,
        )
