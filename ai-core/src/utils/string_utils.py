"""
AI Engineering Framework
String Utilities

Author : TECHAKKENA
"""

import re


class StringUtils:
    """
    Utility methods for string operations.
    """

    @staticmethod
    def is_empty(value: str | None) -> bool:
        """
        Check whether a string is empty.
        """
        return value is None or value.strip() == ""

    @staticmethod
    def truncate(
        value: str,
        length: int,
    ) -> str:
        """
        Truncate a string.
        """
        if len(value) <= length:
            return value

        return value[:length] + "..."

    @staticmethod
    def remove_extra_spaces(
        value: str,
    ) -> str:
        """
        Remove extra whitespace.
        """
        return " ".join(value.split())

    @staticmethod
    def title_case(
        value: str,
    ) -> str:
        """
        Convert to title case.
        """
        return value.title()

    @staticmethod
    def capitalize_words(
        value: str,
    ) -> str:
        """
        Capitalize every word.
        """
        return " ".join(word.capitalize() for word in value.split())

    @staticmethod
    def snake_case(
        value: str,
    ) -> str:
        """
        Convert to snake_case.
        """
        value = re.sub(
            r"([A-Z])",
            r"_\1",
            value,
        )

        return value.strip("_").lower()

    @staticmethod
    def camel_case(
        value: str,
    ) -> str:
        """
        Convert snake_case to camelCase.
        """

        words = value.split("_")

        return words[0].lower() + "".join(word.capitalize() for word in words[1:])

    @staticmethod
    def slugify(
        value: str,
    ) -> str:
        """
        Convert text into URL slug.
        """

        value = value.lower()

        value = re.sub(
            r"[^a-z0-9]+",
            "-",
            value,
        )

        return value.strip("-")
