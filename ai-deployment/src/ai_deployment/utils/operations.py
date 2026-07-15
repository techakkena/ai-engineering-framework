"""
Framework-independent deployment utility operations.
"""

from __future__ import annotations

from urllib.parse import urlparse

from ai_deployment.utils.constants import (
    DEFAULT_ENCODING,
)


class DeploymentUtils:
    """Collection of deployment helper utilities."""

    @staticmethod
    def encode(value: str) -> bytes:
        """Encode a string."""
        return value.encode(DEFAULT_ENCODING)

    @staticmethod
    def decode(value: bytes) -> str:
        """Decode bytes."""
        return value.decode(DEFAULT_ENCODING)

    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Determine whether a URL is valid."""
        parsed = urlparse(url)

        return bool(parsed.scheme and parsed.netloc)

    @staticmethod
    def normalize_image_name(name: str) -> str:
        """Normalize a container image name."""
        return name.strip().lower()

    @staticmethod
    def build_image_reference(
        repository: str,
        tag: str,
    ) -> str:
        """Build a container image reference."""
        return f"{repository}:{tag}"