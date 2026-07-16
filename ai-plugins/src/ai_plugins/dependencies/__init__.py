"""Dependency management utilities for ai-plugins."""

from __future__ import annotations

from ai_plugins.dependencies.operations import (
    DependencyDefinition,
    DependencyRegistry,
    build_dependency,
)

__all__ = [
    "DependencyDefinition",
    "DependencyRegistry",
    "build_dependency",
]