"""Exceptions for prompt loaders."""


class LoaderError(Exception):
    """Base loader exception."""


class PromptFileNotFoundError(LoaderError):
    """Raised when a prompt file cannot be found."""


class UnsupportedPromptFormatError(LoaderError):
    """Raised when an unsupported prompt format is used."""


__all__ = [
    "LoaderError",
    "PromptFileNotFoundError",
    "UnsupportedPromptFormatError",
]
