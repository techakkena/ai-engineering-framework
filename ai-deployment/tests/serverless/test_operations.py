"""
Tests for ai_deployment.serverless.operations.
"""

import pytest

from ai_deployment.serverless.exceptions import (
    ServerlessConfigurationError,
    ServerlessDeploymentError,
)
from ai_deployment.serverless.operations import (
    ServerlessFunction,
    ServerlessService,
)


def test_deploy() -> None:
    service = ServerlessService()

    function = ServerlessFunction(name="predict")

    assert service.deploy(function)


def test_update() -> None:
    service = ServerlessService()

    function = ServerlessFunction(name="predict")

    assert service.update(function)


def test_delete() -> None:
    service = ServerlessService()

    assert service.delete("predict")


def test_invalid_name() -> None:
    service = ServerlessService()

    function = ServerlessFunction(name="")

    with pytest.raises(ServerlessConfigurationError):
        service.deploy(function)


def test_invalid_memory() -> None:
    service = ServerlessService()

    function = ServerlessFunction(
        name="predict",
        memory_mb=0,
    )

    with pytest.raises(ServerlessConfigurationError):
        service.deploy(function)


def test_invalid_timeout() -> None:
    service = ServerlessService()

    function = ServerlessFunction(
        name="predict",
        timeout_seconds=0,
    )

    with pytest.raises(ServerlessConfigurationError):
        service.deploy(function)


def test_invalid_delete() -> None:
    service = ServerlessService()

    with pytest.raises(ServerlessDeploymentError):
        service.delete("")