from __future__ import annotations

"""
AI Engineering Framework
Date Time Utilities

Author : TECHAKKENA
"""

from datetime import date, datetime, timezone


class DateTimeUtils:
    """
    Utility methods for date and time operations.
    """

    @staticmethod
    def now() -> datetime:
        """
        Return current local datetime.
        """
        return datetime.now()

    @staticmethod
    def utc_now() -> datetime:
        """
        Return current UTC datetime.
        """
        return datetime.now(timezone.utc)

    @staticmethod
    def today() -> date:
        """
        Return today's date.
        """
        return date.today()

    @staticmethod
    def timestamp() -> float:
        """
        Return current Unix timestamp.
        """
        return datetime.now().timestamp()

    @staticmethod
    def iso_now() -> str:
        """
        Return current datetime in ISO format.
        """
        return datetime.now().isoformat()

    @staticmethod
    def format(
        dt: datetime,
        fmt: str = "%Y-%m-%d %H:%M:%S",
    ) -> str:
        """
        Format a datetime.
        """
        return dt.strftime(fmt)

    @staticmethod
    def parse(
        value: str,
        fmt: str = "%Y-%m-%d %H:%M:%S",
    ) -> datetime:
        """
        Parse a datetime string.
        """
        return datetime.strptime(value, fmt)
