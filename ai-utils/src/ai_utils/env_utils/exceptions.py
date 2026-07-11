"""
Custom exceptions for the environment utilities package.
"""

from __future__ import annotations

__all__ = [
    "EnvUtilsError",
    "EnvironmentVariableError",
]


class EnvUtilsError(Exception):
    """Base exception for environment utilities."""


class EnvironmentVariableError(EnvUtilsError):
    """Raised when a required environment variable is missing."""
