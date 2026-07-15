"""
Exceptions for the Anthropic provider.

This module defines the exception hierarchy used by the
framework-independent Anthropic provider implementation.
"""

from __future__ import annotations


class AnthropicError(Exception):
    """Base exception for all Anthropic provider errors."""


class AnthropicConfigurationError(AnthropicError):
    """
    Raised when the Anthropic provider configuration is invalid.
    """


class AnthropicAuthenticationError(AnthropicError):
    """
    Raised when authentication with the Anthropic service fails.
    """


class AnthropicRateLimitError(AnthropicError):
    """
    Raised when an Anthropic API rate limit is exceeded.
    """


class AnthropicConnectionError(AnthropicError):
    """
    Raised when communication with the Anthropic service fails.
    """


class AnthropicTimeoutError(AnthropicError):
    """
    Raised when an Anthropic request times out.
    """


class AnthropicModelError(AnthropicError):
    """
    Raised when an invalid or unsupported model is requested.
    """


class AnthropicRequestError(AnthropicError):
    """
    Raised when an invalid request is sent to the Anthropic API.
    """


class AnthropicResponseError(AnthropicError):
    """
    Raised when an invalid response is received from the Anthropic API.
    """


class AnthropicProviderError(AnthropicError):
    """
    Raised for provider-specific runtime errors.
    """