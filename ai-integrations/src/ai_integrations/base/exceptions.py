"""
Shared exceptions for AI provider integrations.

This module defines the common exception hierarchy used by all provider
implementations in the AI Engineering Framework.
"""

from __future__ import annotations


class ProviderError(Exception):
    """
    Base exception for all provider-related errors.
    """


class ProviderConfigurationError(ProviderError):
    """
    Raised when provider configuration is invalid.
    """


class ProviderAuthenticationError(ProviderError):
    """
    Raised when authentication with a provider fails.
    """


class ProviderAuthorizationError(ProviderError):
    """
    Raised when authorization with a provider fails.
    """


class ProviderConnectionError(ProviderError):
    """
    Raised when communication with a provider fails.
    """


class ProviderTimeoutError(ProviderError):
    """
    Raised when a provider request times out.
    """


class ProviderRateLimitError(ProviderError):
    """
    Raised when a provider rate limit is exceeded.
    """


class ProviderRequestError(ProviderError):
    """
    Raised when an invalid request is sent to a provider.
    """


class ProviderResponseError(ProviderError):
    """
    Raised when a provider returns an invalid response.
    """


class ProviderModelError(ProviderError):
    """
    Raised when an invalid or unsupported model is requested.
    """


class ProviderValidationError(ProviderError):
    """
    Raised when request validation fails.
    """


class ProviderStreamingError(ProviderError):
    """
    Raised when a streaming operation fails.
    """


class ProviderEmbeddingError(ProviderError):
    """
    Raised when an embedding operation fails.
    """


class ProviderImageGenerationError(ProviderError):
    """
    Raised when an image generation operation fails.
    """


class ProviderAudioError(ProviderError):
    """
    Raised when an audio operation fails.
    """


class ProviderToolCallError(ProviderError):
    """
    Raised when a tool-calling operation fails.
    """


class ProviderCapabilityError(ProviderError):
    """
    Raised when a requested capability is not supported.
    """