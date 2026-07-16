"""Tests for ai_cloud.providers.exceptions."""

from __future__ import annotations

import pytest

from ai_cloud.providers.exceptions import (
    DuplicateProviderError,
    ProviderError,
    ProviderNotFoundError,
    ProviderRegistrationError,
    ProviderValidationError,
    UnsupportedProviderTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        ProviderValidationError,
        ProviderError,
    )
    assert issubclass(
        ProviderRegistrationError,
        ProviderError,
    )
    assert issubclass(
        ProviderNotFoundError,
        ProviderRegistrationError,
    )
    assert issubclass(
        DuplicateProviderError,
        ProviderRegistrationError,
    )
    assert issubclass(
        UnsupportedProviderTypeError,
        ProviderValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (ProviderError, "base"),
        (ProviderValidationError, "validation"),
        (ProviderRegistrationError, "registration"),
        (ProviderNotFoundError, "missing"),
        (DuplicateProviderError, "duplicate"),
        (UnsupportedProviderTypeError, "provider"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)