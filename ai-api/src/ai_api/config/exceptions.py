"""
Custom exceptions for the ai_api.config module.

This module defines the exception hierarchy used throughout the
configuration components of the AI API package.

All configuration-related exceptions inherit from ``ConfigError``
to provide consistent and predictable error handling.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations


class ConfigError(Exception):
    """
    Base exception for all configuration-related errors.
    """

    def __init__(
        self,
        message: str = "A configuration error occurred.",
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Error message.
        """
        super().__init__(message)


class InvalidConfigurationError(ConfigError):
    """
    Raised when a configuration value is invalid.
    """

    def __init__(
        self,
        key: str,
        value: object,
    ) -> None:
        """
        Initialize the exception.

        Args:
            key: Configuration key.
            value: Invalid configuration value.
        """
        self.key = key
        self.value = value

        super().__init__(
            f"Invalid configuration '{key}': {value!r}."
        )


class MissingConfigurationError(ConfigError):
    """
    Raised when a required configuration value is missing.
    """

    def __init__(
        self,
        key: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            key: Missing configuration key.
        """
        self.key = key

        super().__init__(
            f"Missing required configuration: '{key}'."
        )


class InvalidEnvironmentError(ConfigError):
    """
    Raised when an invalid runtime environment is supplied.
    """

    def __init__(
        self,
        environment: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            environment: Invalid environment name.
        """
        self.environment = environment

        super().__init__(
            f"Invalid environment: '{environment}'."
        )


class UnsupportedConfigurationError(ConfigError):
    """
    Raised when a configuration option is unsupported.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            configuration: Unsupported configuration option.
        """
        self.configuration = configuration

        super().__init__(
            f"Unsupported configuration: '{configuration}'."
        )


class ConfigurationValidationError(ConfigError):
    """
    Raised when configuration validation fails.
    """

    def __init__(
        self,
        key: str,
        reason: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            key: Configuration key.
            reason: Validation failure reason.
        """
        self.key = key
        self.reason = reason

        super().__init__(
            f"Configuration validation failed for '{key}': {reason}."
        )


class ConfigurationFileError(ConfigError):
    """
    Raised when a configuration file cannot be loaded.
    """

    def __init__(
        self,
        filename: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            filename: Configuration filename.
        """
        self.filename = filename

        super().__init__(
            f"Unable to load configuration file: '{filename}'."
        )


class ConfigurationParseError(ConfigError):
    """
    Raised when a configuration file cannot be parsed.
    """

    def __init__(
        self,
        filename: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            filename: Configuration filename.
        """
        self.filename = filename

        super().__init__(
            f"Unable to parse configuration file: '{filename}'."
        )