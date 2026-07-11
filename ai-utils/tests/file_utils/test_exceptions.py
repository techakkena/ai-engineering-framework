"""
Unit tests for file utility exceptions.
"""

from __future__ import annotations

import pytest

from ai_utils.file_utils.exceptions import (
    DirectoryCreationError,
    FileOperationError,
    FileReadError,
    FileUtilsError,
    FileWriteError,
)


def test_file_utils_error_is_exception() -> None:
    assert issubclass(FileUtilsError, Exception)


def test_file_read_error_inherits_base() -> None:
    assert issubclass(FileReadError, FileUtilsError)


def test_file_write_error_inherits_base() -> None:
    assert issubclass(FileWriteError, FileUtilsError)


def test_file_operation_error_inherits_base() -> None:
    assert issubclass(FileOperationError, FileUtilsError)


def test_directory_creation_error_inherits_base() -> None:
    assert issubclass(DirectoryCreationError, FileUtilsError)


@pytest.mark.parametrize(
    "exception_class",
    [
        FileUtilsError,
        FileReadError,
        FileWriteError,
        FileOperationError,
        DirectoryCreationError,
    ],
)
def test_exception_can_be_raised(
    exception_class: type[Exception],
) -> None:
    with pytest.raises(exception_class):
        raise exception_class("Test exception")
