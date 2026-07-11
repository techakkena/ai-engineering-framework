"""
AI Engineering Framework
Validation Utilities

Author : TECHAKKENA
"""

import ipaddress
import json
import re
from pathlib import Path
from urllib.parse import urlparse
from uuid import UUID


class ValidationUtils:
    """
    Utility methods for common validations.
    """

    @staticmethod
    def is_empty(value: str | None) -> bool:
        """
        Check whether a string is empty.
        """
        return value is None or value.strip() == ""

    @staticmethod
    def is_email(email: str) -> bool:
        """
        Validate email address.
        """
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        return re.match(pattern, email) is not None

    @staticmethod
    def is_url(url: str) -> bool:
        """
        Validate URL.
        """

        parsed = urlparse(url)

        return bool(parsed.scheme and parsed.netloc)

    @staticmethod
    def is_uuid(value: str) -> bool:
        """
        Validate UUID.
        """

        try:
            UUID(value)

            return True

        except ValueError:
            return False

    @staticmethod
    def is_json(value: str) -> bool:
        """
        Validate JSON string.
        """

        try:
            json.loads(value)

            return True

        except Exception:
            return False

    @staticmethod
    def is_number(value: str) -> bool:
        """
        Validate numeric value.
        """

        try:
            float(value)

            return True

        except ValueError:
            return False

    @staticmethod
    def is_ip_address(value: str) -> bool:
        """
        Validate IPv4 or IPv6 address.
        """

        try:
            ipaddress.ip_address(value)

            return True

        except ValueError:
            return False

    @staticmethod
    def is_filename(path: str) -> bool:
        """
        Validate filename.
        """

        return Path(path).name == path

    @staticmethod
    def has_extension(
        filename: str,
        *extensions: str,
    ) -> bool:
        """
        Validate file extension.
        """

        return Path(filename).suffix.lower() in {ext.lower() for ext in extensions}
