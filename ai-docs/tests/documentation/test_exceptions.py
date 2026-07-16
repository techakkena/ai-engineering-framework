"""Tests for ai_docs.documentation.exceptions."""

from __future__ import annotations

import pytest

from ai_docs.documentation.exceptions import (
    DocumentationError,
    DocumentationNotFoundError,
    DocumentationRegistrationError,
    DocumentationValidationError,
    DuplicateDocumentationError,
    UnsupportedDocumentationTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        DocumentationValidationError,
        DocumentationError,
    )
    assert issubclass(
        DocumentationRegistrationError,
        DocumentationError,
    )
    assert issubclass(
        DocumentationNotFoundError,
        DocumentationRegistrationError,
    )
    assert issubclass(
        DuplicateDocumentationError,
        DocumentationRegistrationError,
    )
    assert issubclass(
        UnsupportedDocumentationTypeError,
        DocumentationValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (DocumentationError, "base"),
        (
            DocumentationValidationError,
            "validation",
        ),
        (
            DocumentationRegistrationError,
            "registration",
        ),
        (
            DocumentationNotFoundError,
            "missing",
        ),
        (
            DuplicateDocumentationError,
            "duplicate",
        ),
        (
            UnsupportedDocumentationTypeError,
            "type",
        ),
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