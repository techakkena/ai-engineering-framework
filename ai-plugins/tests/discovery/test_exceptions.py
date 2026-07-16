"""Tests for ai_plugins.discovery.exceptions."""

from __future__ import annotations

import pytest

from ai_plugins.discovery.exceptions import (
    DiscoveryError,
    DiscoveryNotFoundError,
    DiscoveryRegistrationError,
    DiscoveryValidationError,
    DuplicateDiscoveryError,
    UnsupportedDiscoveryStrategyError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        DiscoveryValidationError,
        DiscoveryError,
    )
    assert issubclass(
        DiscoveryRegistrationError,
        DiscoveryError,
    )
    assert issubclass(
        DiscoveryNotFoundError,
        DiscoveryRegistrationError,
    )
    assert issubclass(
        DuplicateDiscoveryError,
        DiscoveryRegistrationError,
    )
    assert issubclass(
        UnsupportedDiscoveryStrategyError,
        DiscoveryValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (DiscoveryError, "base"),
        (DiscoveryValidationError, "validation"),
        (DiscoveryRegistrationError, "registration"),
        (DiscoveryNotFoundError, "missing"),
        (DuplicateDiscoveryError, "duplicate"),
        (UnsupportedDiscoveryStrategyError, "strategy"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)