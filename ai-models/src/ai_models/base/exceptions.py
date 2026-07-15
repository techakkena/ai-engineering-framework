"""
Exceptions for ai_models.base.
"""

from __future__ import annotations


class BaseModelError(Exception):
    """
    Base model exception.
    """

    def __init__(
        self,
        message: str = "A model error occurred.",
    ) -> None:
        super().__init__(message)


class InvalidModelTypeError(BaseModelError):
    """
    Raised when an invalid model type is supplied.
    """

    def __init__(
        self,
        model_type: str,
    ) -> None:
        self.model_type = model_type

        super().__init__(
            f"Invalid model type: '{model_type}'."
        )


class ModelConfigurationError(BaseModelError):
    """
    Raised when model configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        self.configuration = configuration

        super().__init__(
            f"Invalid model configuration: '{configuration}'."
        )


class ModelValidationError(BaseModelError):
    """
    Raised when model validation fails.
    """

    def __init__(
        self,
        model: str,
        reason: str,
    ) -> None:
        self.model = model
        self.reason = reason

        super().__init__(
            f"Model '{model}' validation failed: {reason}."
        )