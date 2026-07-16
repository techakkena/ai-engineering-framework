"""Tests for ai_docs.schemas.exceptions."""

from __future__ import annotations

import pytest

from ai_docs.schemas.exceptions import (
    DuplicateSchemaError,
    SchemaError,
    SchemaNotFoundError,
    SchemaRegistrationError,
    SchemaValidationError,
    UnsupportedSchemaFormatError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        SchemaValidationError,
        SchemaError,
    )
    assert issubclass(
        SchemaRegistrationError,
        SchemaError,
    )
    assert issubclass(
        SchemaNotFoundError,
        SchemaRegistrationError,
    )
    assert issubclass(
        DuplicateSchemaError,
        SchemaRegistrationError,
    )
    assert issubclass(
        UnsupportedSchemaFormatError,
        SchemaValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (SchemaError, "base"),
        (SchemaValidationError, "validation"),
        (SchemaRegistrationError, "registration"),
        (SchemaNotFoundError, "missing"),
        (DuplicateSchemaError, "duplicate"),
        (UnsupportedSchemaFormatError, "format"),
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