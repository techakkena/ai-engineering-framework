"""Exceptions for the ai_docs.templates module."""

from __future__ import annotations


class TemplateError(Exception):
    """Base exception for template operations."""


class TemplateValidationError(
    TemplateError,
):
    """Raised when template validation fails."""


class TemplateRegistrationError(
    TemplateError,
):
    """Raised when template registration fails."""


class TemplateNotFoundError(
    TemplateRegistrationError,
):
    """Raised when a template cannot be found."""


class DuplicateTemplateError(
    TemplateRegistrationError,
):
    """Raised when attempting to register a duplicate template."""


class UnsupportedTemplateTypeError(
    TemplateValidationError,
):
    """Raised when an unsupported template type is specified."""


__all__ = [
    "DuplicateTemplateError",
    "TemplateError",
    "TemplateNotFoundError",
    "TemplateRegistrationError",
    "TemplateValidationError",
    "UnsupportedTemplateTypeError",
]