"""Exceptions for the ai_plugins.registry module."""

from __future__ import annotations


class PluginError(Exception):
    """Base exception for plugin operations."""


class PluginValidationError(PluginError):
    """Raised when plugin validation fails."""


class PluginRegistrationError(PluginError):
    """Raised when plugin registration fails."""


class PluginNotFoundError(PluginRegistrationError):
    """Raised when a requested plugin cannot be found."""


class DuplicatePluginError(PluginRegistrationError):
    """Raised when attempting to register a duplicate plugin."""


class UnsupportedPluginStateError(
    PluginValidationError,
):
    """Raised when an unsupported plugin state is specified."""


__all__ = [
    "DuplicatePluginError",
    "PluginError",
    "PluginNotFoundError",
    "PluginRegistrationError",
    "PluginValidationError",
    "UnsupportedPluginStateError",
]