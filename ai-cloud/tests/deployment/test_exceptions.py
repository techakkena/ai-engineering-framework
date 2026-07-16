"""Tests for ai_cloud.deployment.exceptions."""

from __future__ import annotations

import pytest

from ai_cloud.deployment.exceptions import (
    DeploymentError,
    DeploymentNotFoundError,
    DeploymentRegistrationError,
    DeploymentValidationError,
    DuplicateDeploymentError,
    UnsupportedDeploymentStrategyError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        DeploymentValidationError,
        DeploymentError,
    )
    assert issubclass(
        DeploymentRegistrationError,
        DeploymentError,
    )
    assert issubclass(
        DeploymentNotFoundError,
        DeploymentRegistrationError,
    )
    assert issubclass(
        DuplicateDeploymentError,
        DeploymentRegistrationError,
    )
    assert issubclass(
        UnsupportedDeploymentStrategyError,
        DeploymentValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (DeploymentError, "base"),
        (DeploymentValidationError, "validation"),
        (DeploymentRegistrationError, "registration"),
        (DeploymentNotFoundError, "missing"),
        (DuplicateDeploymentError, "duplicate"),
        (
            UnsupportedDeploymentStrategyError,
            "strategy",
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