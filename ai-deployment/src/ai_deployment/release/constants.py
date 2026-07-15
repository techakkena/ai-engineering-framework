"""
Constants for the release module.
"""

from __future__ import annotations

DEFAULT_RELEASE_CHANNEL: str = "stable"

DEFAULT_VERSION_PREFIX: str = "v"

SUPPORTED_RELEASE_CHANNELS: frozenset[str] = frozenset(
    {
        "alpha",
        "beta",
        "rc",
        "stable",
    }
)