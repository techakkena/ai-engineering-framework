"""Tests for ai_testing.snapshots.exceptions."""

from __future__ import annotations

import pytest

from ai_testing.snapshots.exceptions import (
    DuplicateSnapshotError,
    SnapshotError,
    SnapshotNotFoundError,
    SnapshotRegistrationError,
    SnapshotValidationError,
    UnsupportedSnapshotFormatError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(SnapshotValidationError, SnapshotError)
    assert issubclass(SnapshotRegistrationError, SnapshotError)
    assert issubclass(SnapshotNotFoundError, SnapshotRegistrationError)
    assert issubclass(DuplicateSnapshotError, SnapshotRegistrationError)
    assert issubclass(
        UnsupportedSnapshotFormatError,
        SnapshotValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (SnapshotError, "base"),
        (SnapshotValidationError, "validation"),
        (SnapshotRegistrationError, "registration"),
        (SnapshotNotFoundError, "missing"),
        (DuplicateSnapshotError, "duplicate"),
        (UnsupportedSnapshotFormatError, "format"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)