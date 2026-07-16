"""Exceptions for the ai_plugins.sandbox module."""

from __future__ import annotations


class SandboxError(Exception):
    """Base exception for sandbox operations."""


class SandboxValidationError(SandboxError):
    """Raised when sandbox validation fails."""


class SandboxRegistrationError(SandboxError):
    """Raised when sandbox registration fails."""


class SandboxNotFoundError(
    SandboxRegistrationError,
):
    """Raised when a sandbox definition cannot be found."""


class DuplicateSandboxError(
    SandboxRegistrationError,
):
    """Raised when attempting to register a duplicate sandbox."""


class UnsupportedSandboxModeError(
    SandboxValidationError,
):
    """Raised when an unsupported sandbox mode is specified."""


__all__ = [
    "DuplicateSandboxError",
    "SandboxError",
    "SandboxNotFoundError",
    "SandboxRegistrationError",
    "SandboxValidationError",
    "UnsupportedSandboxModeError",
]