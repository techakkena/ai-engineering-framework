"""
AI Engineering Framework
Base Exception

Author : TECHAKKENA
"""

from datetime import datetime
from typing import Any


class FrameworkException(Exception):
    """
    Base class for all framework exceptions.
    """

    def __init__(
        self,
        message: str,
        error_code: str = "BASE001",
        status_code: int = 500,
        module: str = "Framework",
        details: Any = None,
    ):

        super().__init__(message)

        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        self.module = module
        self.details = details
        self.timestamp = datetime.now()

    def to_dict(self) -> dict:
        """
        Convert exception to dictionary.
        """

        return {
            "message": self.message,
            "error_code": self.error_code,
            "status_code": self.status_code,
            "module": self.module,
            "details": self.details,
            "timestamp": self.timestamp.isoformat(),
        }

    def __str__(self) -> str:

        return f"[{self.error_code}] {self.message}"
