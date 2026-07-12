"""
Custom exceptions for the loader module.

Author: TECHAKKENA
"""


class LoaderError(Exception):
    """Base exception for loader operations."""


class UnsupportedFormatError(LoaderError):
    """Raised when an unsupported configuration format is provided."""


class ConfigurationNotFoundError(LoaderError):
    """Raised when the configuration file cannot be found."""


class ConfigurationParseError(LoaderError):
    """Raised when a configuration file cannot be parsed."""
