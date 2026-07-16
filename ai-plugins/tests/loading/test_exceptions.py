"""Tests for ai_plugins.loading.exceptions."""

from __future__ import annotations

import pytest

from ai_plugins.loading.exceptions import (
    DuplicateLoaderError,
    LoaderError,
    LoaderNotFoundError,
    LoaderRegistrationError,
    LoaderValidationError,
    UnsupportedLoadingModeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        LoaderValidationError,
        LoaderError,
    )
    assert issubclass(
        LoaderRegistrationError,
        LoaderError,
    )
    assert issubclass(
        LoaderNotFoundError,
        LoaderRegistrationError,
    )
    assert issubclass(
        DuplicateLoaderError,
        LoaderRegistrationError,
    )
    assert issubclass(
        UnsupportedLoadingModeError,
        LoaderValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (LoaderError, "base"),
        (LoaderValidationError, "validation"),
        (LoaderRegistrationError, "registration"),
        (LoaderNotFoundError, "missing"),
        (DuplicateLoaderError, "duplicate"),
        (UnsupportedLoadingModeError, "mode"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)