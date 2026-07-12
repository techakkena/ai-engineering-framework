"""
Environment management for ai-config.

This module provides utilities for loading and accessing
environment variables from the operating system and .env files.
"""

from ai_config.environment.operations import EnvironmentLoader

__all__ = [
    "EnvironmentLoader",
]
