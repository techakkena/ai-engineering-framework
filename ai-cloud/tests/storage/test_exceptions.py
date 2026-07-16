"""Tests for ai_cloud.storage.exceptions."""

from __future__ import annotations

import pytest

from ai_cloud.storage.exceptions import (
    DuplicateStorageError,
    StorageError,
    StorageNotFoundError,
    StorageRegistrationError,
    StorageValidationError,
    UnsupportedStorageTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        StorageValidationError,
        StorageError,
    )
    assert issubclass(
        StorageRegistrationError,
        StorageError,
    )
    assert issubclass(
        StorageNotFoundError,
        StorageRegistrationError,
    )
    assert issubclass(
        DuplicateStorageError,
        StorageRegistrationError,
    )
    assert issubclass(
        UnsupportedStorageTypeError,
        StorageValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (StorageError, "base"),
        (StorageValidationError, "validation"),
        (StorageRegistrationError, "registration"),
        (StorageNotFoundError, "missing"),
        (DuplicateStorageError, "duplicate"),
        (UnsupportedStorageTypeError, "storage"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)