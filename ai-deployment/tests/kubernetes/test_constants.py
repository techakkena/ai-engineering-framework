"""
Tests for ai_deployment.kubernetes.constants.
"""

from ai_deployment.kubernetes.constants import (
    DEFAULT_NAMESPACE,
    DEFAULT_REPLICAS,
    DEFAULT_SERVICE_TYPE,
)


def test_default_namespace() -> None:
    assert DEFAULT_NAMESPACE == "default"


def test_default_replicas() -> None:
    assert DEFAULT_REPLICAS == 1


def test_default_service_type() -> None:
    assert DEFAULT_SERVICE_TYPE == "ClusterIP"