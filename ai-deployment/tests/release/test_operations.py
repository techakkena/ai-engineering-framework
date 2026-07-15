"""
Tests for ai_deployment.release.operations.
"""

import pytest

from ai_deployment.release.exceptions import (
    ReleaseConfigurationError,
    ReleaseValidationError,
)
from ai_deployment.release.operations import (
    Release,
    ReleaseService,
)


def test_full_version() -> None:
    release = Release(version="1.2.3")

    assert release.full_version == "v1.2.3"


def test_validate_release() -> None:
    service = ReleaseService()

    release = Release(version="1.0.0")

    assert service.validate(release)


def test_publish_release() -> None:
    service = ReleaseService()

    release = Release(version="1.0.0")

    assert service.publish(release)


def test_rollback_release() -> None:
    service = ReleaseService()

    release = Release(version="1.0.0")

    assert service.rollback(release)


def test_invalid_release_version() -> None:
    service = ReleaseService()

    release = Release(version="")

    with pytest.raises(ReleaseValidationError):
        service.validate(release)


def test_invalid_release_channel() -> None:
    service = ReleaseService()

    release = Release(
        version="1.0.0",
        channel="nightly",
    )

    with pytest.raises(ReleaseConfigurationError):
        service.validate(release)