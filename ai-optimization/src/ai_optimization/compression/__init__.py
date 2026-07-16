"""Compression utilities for ai-optimization."""

from __future__ import annotations

from ai_optimization.compression.operations import (
    CompressionDefinition,
    CompressionRegistry,
    build_compression,
)

__all__ = [
    "CompressionDefinition",
    "CompressionRegistry",
    "build_compression",
]