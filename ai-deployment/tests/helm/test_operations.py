"""
Tests for ai_deployment.helm.operations.
"""

import pytest

from ai_deployment.helm.exceptions import (
    HelmConfigurationError,
    HelmDeploymentError,
)
from ai_deployment.helm.operations import (
    HelmChart,
    HelmService,
)


def test_install() -> None:
    service = HelmService()

    chart = HelmChart(chart="ai-api")

    assert service.install(chart)


def test_upgrade() -> None:
    service = HelmService()

    chart = HelmChart(
        chart="ai-api",
        release="production",
    )

    assert service.upgrade(chart)


def test_uninstall() -> None:
    service = HelmService()

    assert service.uninstall("production")


def test_install_invalid_chart() -> None:
    service = HelmService()

    chart = HelmChart(chart="")

    with pytest.raises(HelmConfigurationError):
        service.install(chart)


def test_upgrade_invalid_release() -> None:
    service = HelmService()

    chart = HelmChart(
        chart="ai-api",
        release="",
    )

    with pytest.raises(HelmDeploymentError):
        service.upgrade(chart)


def test_uninstall_invalid_release() -> None:
    service = HelmService()

    with pytest.raises(HelmConfigurationError):
        service.uninstall("")