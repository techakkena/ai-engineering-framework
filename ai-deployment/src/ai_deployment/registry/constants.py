"""
Constants for the registry module.
"""

from __future__ import annotations

DEFAULT_REGISTRY: str = "docker.io"

DEFAULT_REPOSITORY: str = "library"

SUPPORTED_REGISTRIES: frozenset[str] = frozenset(
    {
        "docker.io",
        "ghcr.io",
        "gcr.io",
        "quay.io",
        "ecr",
        "acr",
    }
)