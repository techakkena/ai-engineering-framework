"""
Unit tests for ai_models.base.exceptions.
"""

from __future__ import annotations

import pytest

from ai_models.base.exceptions import (
    BaseModelError,
    InvalidModelTypeError,
    ModelConfigurationError,
    ModelValidationError,
)


def test_base_model_error_default_message() -> None:
    error = BaseModelError()
    assert str(error) == "A model error occurred."


def test_base_model_error_custom_message() -> None:
    error = BaseModelError("Custom model error.")
    assert str(error) == "Custom model error."


@pytest.mark.parametrize(
    "model_type",
    ["", "text", "image"],
)
def test_invalid_model_type_error(
    model_type: str,
) -> None:
    error = InvalidModelTypeError(model_type)

    assert isinstance(error, BaseModelError)
    assert error.model_type == model_type
    assert (
        str(error)
        == f"Invalid model type: '{model_type}'."
    )


def test_model_configuration_error() -> None:
    error = ModelConfigurationError("temperature")

    assert error.configuration == "temperature"


def test_model_validation_error() -> None:
    error = ModelValidationError(
        "gpt-5",
        "invalid configuration",
    )

    assert error.model == "gpt-5"
    assert error.reason == "invalid configuration"