from __future__ import annotations

"""
AI Engineering Framework
AI Exception

Author : TECHAKKENA
"""

from typing import Any

from .base_exception import FrameworkException
from .error_codes import ErrorCode


class AIException(FrameworkException):
    """
    Exception raised for AI model failures.
    """

    def __init__(
        self,
        message: str = "AI operation failed.",
        details: Any = None,
    ):

        super().__init__(
            message=message,
            error_code=ErrorCode.AI_ERROR.value,
            status_code=500,
            module="AI",
            details=details,
        )
