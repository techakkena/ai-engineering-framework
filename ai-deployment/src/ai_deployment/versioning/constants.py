"""
Constants for the versioning module.
"""

from __future__ import annotations

DEFAULT_INITIAL_VERSION: str = "0.1.0"

DEFAULT_VERSION_SEPARATOR: str = "."

SEMVER_PARTS: tuple[str, str, str] = (
    "major",
    "minor",
    "patch",
)