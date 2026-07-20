from __future__ import annotations

"""Exceptions for prompt registry."""


class RegistryError(Exception):
    """Base registry exception."""


class PromptAlreadyRegisteredError(RegistryError):
    """Raised when a prompt is already registered."""


class PromptNotRegisteredError(RegistryError):
    """Raised when a prompt is not registered."""


__all__ = [
    "RegistryError",
    "PromptAlreadyRegisteredError",
    "PromptNotRegisteredError",
]
