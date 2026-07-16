"""Tests for ai_docs.openapi.exceptions."""

from __future__ import annotations

import pytest

from ai_docs.openapi.exceptions import (
    DuplicateOpenAPIError,
    OpenAPIError,
    OpenAPINotFoundError,
    OpenAPIRegistrationError,
    OpenAPIValidationError,
    UnsupportedOpenAPIVersionError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        OpenAPIValidationError,
        OpenAPIError,
    )
    assert issubclass(
        OpenAPIRegistrationError,
        OpenAPIError,
    )
    assert issubclass(
        OpenAPINotFoundError,
        OpenAPIRegistrationError,
    )
    assert issubclass(
        DuplicateOpenAPIError,
        OpenAPIRegistrationError,
    )
    assert issubclass(
        UnsupportedOpenAPIVersionError,
        OpenAPIValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (OpenAPIError, "base"),
        (OpenAPIValidationError, "validation"),
        (OpenAPIRegistrationError, "registration"),
        (OpenAPINotFoundError, "missing"),
        (DuplicateOpenAPIError, "duplicate"),
        (UnsupportedOpenAPIVersionError, "version"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(
        exception_class,
        match=message,
    ):
        raise exception_class(message)