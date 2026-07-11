"""
Decorators for the AI Engineering Framework.

This package provides reusable decorators for timing,
deprecation warnings, singleton classes, and
thread synchronization.
"""

from __future__ import annotations

from ai_utils.decorators.operations import (
    deprecated,
    singleton,
    synchronized,
    timer,
)

__all__ = [
    "deprecated",
    "singleton",
    "synchronized",
    "timer",
]
