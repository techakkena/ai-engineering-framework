"""Exceptions for the ai_docs.generators module."""

from __future__ import annotations


class GeneratorError(Exception):
    """Base exception for generator operations."""


class GeneratorValidationError(
    GeneratorError,
):
    """Raised when generator validation fails."""


class GeneratorRegistrationError(
    GeneratorError,
):
    """Raised when generator registration fails."""


class GeneratorNotFoundError(
    GeneratorRegistrationError,
):
    """Raised when a generator cannot be found."""


class DuplicateGeneratorError(
    GeneratorRegistrationError,
):
    """Raised when attempting to register a duplicate generator."""


class UnsupportedGeneratorTypeError(
    GeneratorValidationError,
):
    """Raised when an unsupported generator type is specified."""


__all__ = [
    "DuplicateGeneratorError",
    "GeneratorError",
    "GeneratorNotFoundError",
    "GeneratorRegistrationError",
    "GeneratorValidationError",
    "UnsupportedGeneratorTypeError",
]