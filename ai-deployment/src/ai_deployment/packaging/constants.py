"""
Constants for the packaging module.
"""

from __future__ import annotations

DEFAULT_BUILD_DIRECTORY: str = "dist"

DEFAULT_PACKAGE_FORMAT: str = "wheel"

SUPPORTED_PACKAGE_FORMATS: frozenset[str] = frozenset(
    {
        "wheel",
        "sdist",
        "docker",
        "zip",
        "tar.gz",
    }
)