"""Tests for ai_docs.templates.exceptions."""

from __future__ import annotations

import pytest

from ai_docs.templates.exceptions import (
    DuplicateTemplateError,
    TemplateError,
    TemplateNotFoundError,
    TemplateRegistrationError,
    TemplateValidationError,
    UnsupportedTemplateTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        TemplateValidationError,
        TemplateError,
    )
    assert issubclass(
        TemplateRegistrationError,
        TemplateError,
    )
    assert issubclass(
        TemplateNotFoundError,
        TemplateRegistrationError,
    )
    assert issubclass(
        DuplicateTemplateError,
        TemplateRegistrationError,
    )
    assert issubclass(
        UnsupportedTemplateTypeError,
        TemplateValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (TemplateError, "base"),
        (TemplateValidationError, "validation"),
        (TemplateRegistrationError, "registration"),
        (TemplateNotFoundError, "missing"),
        (DuplicateTemplateError, "duplicate"),
        (UnsupportedTemplateTypeError, "type"),
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