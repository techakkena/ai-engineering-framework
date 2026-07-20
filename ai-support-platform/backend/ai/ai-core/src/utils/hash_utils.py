from __future__ import annotations

"""
AI Engineering Framework
Hash Utilities

Author : TECHAKKENA
"""

import hashlib
from pathlib import Path


class HashUtils:
    """
    Utility methods for hashing.
    """

    @staticmethod
    def md5(data: str) -> str:
        """
        Generate MD5 hash.
        """
        return hashlib.md5(data.encode("utf-8")).hexdigest()

    @staticmethod
    def sha1(data: str) -> str:
        """
        Generate SHA1 hash.
        """
        return hashlib.sha1(data.encode("utf-8")).hexdigest()

    @staticmethod
    def sha256(data: str) -> str:
        """
        Generate SHA256 hash.
        """
        return hashlib.sha256(data.encode("utf-8")).hexdigest()

    @staticmethod
    def sha512(data: str) -> str:
        """
        Generate SHA512 hash.
        """
        return hashlib.sha512(data.encode("utf-8")).hexdigest()

    @staticmethod
    def file_sha256(
        file_path: Path,
    ) -> str:
        """
        Generate SHA256 hash for a file.
        """

        sha = hashlib.sha256()

        with file_path.open("rb") as file:
            while chunk := file.read(8192):
                sha.update(chunk)

        return sha.hexdigest()

    @staticmethod
    def verify_sha256(
        data: str,
        expected_hash: str,
    ) -> bool:
        """
        Verify SHA256 hash.
        """

        return HashUtils.sha256(data) == expected_hash
