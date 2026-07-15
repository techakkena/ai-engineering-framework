"""
Tests for ai_deployment.utils.operations.
"""

from ai_deployment.utils.operations import (
    DeploymentUtils,
)


def test_encode() -> None:
    encoded = DeploymentUtils.encode("hello")

    assert encoded == b"hello"


def test_decode() -> None:
    decoded = DeploymentUtils.decode(b"hello")

    assert decoded == "hello"


def test_valid_url() -> None:
    assert DeploymentUtils.is_valid_url(
        "https://openai.com"
    )


def test_invalid_url() -> None:
    assert not DeploymentUtils.is_valid_url(
        "invalid-url"
    )


def test_normalize_image_name() -> None:
    assert (
        DeploymentUtils.normalize_image_name(
            "  AI-Framework/API  "
        )
        == "ai-framework/api"
    )


def test_build_image_reference() -> None:
    assert (
        DeploymentUtils.build_image_reference(
            "ai-framework/api",
            "1.0.0",
        )
        == "ai-framework/api:1.0.0"
    )