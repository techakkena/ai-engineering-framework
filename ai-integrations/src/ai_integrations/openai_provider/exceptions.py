"""
Exceptions for the OpenAI provider.

This module defines the exception hierarchy used by the
framework-independent OpenAI provider implementation.
"""

from __future__ import annotations


class OpenAIError(Exception):
    """Base exception for all OpenAI provider errors."""


class OpenAIConfigurationError(OpenAIError):
    """
    Raised when the OpenAI provider configuration is invalid.
    """


class OpenAIAuthenticationError(OpenAIError):
    """
    Raised when authentication with the OpenAI service fails.
    """


class OpenAIRateLimitError(OpenAIError):
    """
    Raised when an OpenAI API rate limit is exceeded.
    """


class OpenAIConnectionError(OpenAIError):
    """
    Raised when communication with the OpenAI service fails.
    """


class OpenAITimeoutError(OpenAIError):
    """
    Raised when an OpenAI request times out.
    """


class OpenAIModelError(OpenAIError):
    """
    Raised when an invalid or unsupported model is requested.
    """


class OpenAIRequestError(OpenAIError):
    """
    Raised when an invalid request is sent to the OpenAI API.
    """


class OpenAIResponseError(OpenAIError):
    """
    Raised when an invalid response is received from the OpenAI API.
    """


class OpenAIProviderError(OpenAIError):
    """
    Raised for provider-specific runtime errors.
    """