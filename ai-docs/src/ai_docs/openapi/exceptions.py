"""Exceptions for the ai_docs.openapi module."""

from __future__ import annotations


class OpenAPIError(Exception):
    """Base exception for OpenAPI operations."""


class OpenAPIValidationError(OpenAPIError):
    """Raised when OpenAPI validation fails."""


class OpenAPIRegistrationError(OpenAPIError):
    """Raised when OpenAPI registration fails."""


class OpenAPINotFoundError(
    OpenAPIRegistrationError,
):
    """Raised when an OpenAPI document cannot be found."""


class DuplicateOpenAPIError(
    OpenAPIRegistrationError,
):
    """Raised when attempting to register a duplicate OpenAPI document."""


class UnsupportedOpenAPIVersionError(
    OpenAPIValidationError,
):
    """Raised when an unsupported OpenAPI version is specified."""


__all__ = [
    "DuplicateOpenAPIError",
    "OpenAPIError",
    "OpenAPINotFoundError",
    "OpenAPIRegistrationError",
    "OpenAPIValidationError",
    "UnsupportedOpenAPIVersionError",
]