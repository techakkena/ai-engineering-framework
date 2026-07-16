"""Tests for ai_docs.exporters.exceptions."""

from __future__ import annotations

import pytest

from ai_docs.exporters.exceptions import (
    DuplicateExportError,
    ExportError,
    ExportNotFoundError,
    ExportRegistrationError,
    ExportValidationError,
    UnsupportedExportFormatError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        ExportValidationError,
        ExportError,
    )
    assert issubclass(
        ExportRegistrationError,
        ExportError,
    )
    assert issubclass(
        ExportNotFoundError,
        ExportRegistrationError,
    )
    assert issubclass(
        DuplicateExportError,
        ExportRegistrationError,
    )
    assert issubclass(
        UnsupportedExportFormatError,
        ExportValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (ExportError, "base"),
        (ExportValidationError, "validation"),
        (ExportRegistrationError, "registration"),
        (ExportNotFoundError, "missing"),
        (DuplicateExportError, "duplicate"),
        (UnsupportedExportFormatError, "format"),
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