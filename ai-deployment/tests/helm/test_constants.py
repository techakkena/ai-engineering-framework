"""
Tests for ai_deployment.helm.constants.
"""

from ai_deployment.helm.constants import (
    DEFAULT_CHART_VERSION,
    DEFAULT_NAMESPACE,
    DEFAULT_RELEASE_NAME,
)


def test_default_release_name() -> None:
    assert DEFAULT_RELEASE_NAME == "ai-framework"


def test_default_namespace() -> None:
    assert DEFAULT_NAMESPACE == "default"


def test_default_chart_version() -> None:
    assert DEFAULT_CHART_VERSION == "latest"