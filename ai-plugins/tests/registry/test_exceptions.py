"""Tests for ai_plugins.registry.exceptions."""

from __future__ import annotations

import pytest

from ai_plugins.registry.exceptions import (
    DuplicatePluginError,
    PluginError,
    PluginNotFoundError,
    PluginRegistrationError,
    PluginValidationError,
    UnsupportedPluginStateError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        PluginValidationError,
        PluginError,
    )
    assert issubclass(
        PluginRegistrationError,
        PluginError,
    )
    assert issubclass(
        PluginNotFoundError,
        PluginRegistrationError,
    )
    assert issubclass(
        DuplicatePluginError,
        PluginRegistrationError,
    )
    assert issubclass(
        UnsupportedPluginStateError,
        PluginValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (PluginError, "base"),
        (PluginValidationError, "validation"),
        (PluginRegistrationError, "registration"),
        (PluginNotFoundError, "missing"),
        (DuplicatePluginError, "duplicate"),
        (UnsupportedPluginStateError, "state"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)