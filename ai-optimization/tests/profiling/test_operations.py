"""Tests for ai_optimization.profiling.operations."""

from __future__ import annotations

import pytest

from ai_optimization.profiling.constants import (
    DEFAULT_ENABLED,
    DEFAULT_PROFILE_TYPE,
)
from ai_optimization.profiling.exceptions import (
    DuplicateProfileError,
    ProfileNotFoundError,
    ProfileValidationError,
    UnsupportedProfileTypeError,
)
from ai_optimization.profiling.operations import (
    ProfileDefinition,
    ProfileRegistry,
    build_profile,
)


def test_profile_definition_defaults() -> None:
    profile = ProfileDefinition(
        name="default",
        interval=1.0,
    )

    assert profile.name == "default"
    assert profile.interval == 1.0
    assert profile.profile_type == DEFAULT_PROFILE_TYPE
    assert profile.description == ""
    assert profile.enabled is DEFAULT_ENABLED


def test_profile_definition_trims_name() -> None:
    profile = ProfileDefinition(
        name="  default  ",
        interval=1.0,
    )

    assert profile.name == "default"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(ProfileValidationError):
        ProfileDefinition(
            name=name,
            interval=1.0,
        )


@pytest.mark.parametrize(
    "interval",
    [
        0.0,
        -0.1,
        -1.0,
    ],
)
def test_invalid_interval(interval: float) -> None:
    with pytest.raises(ProfileValidationError):
        ProfileDefinition(
            name="default",
            interval=interval,
        )


def test_invalid_profile_type() -> None:
    with pytest.raises(
        UnsupportedProfileTypeError,
    ):
        ProfileDefinition(
            name="default",
            interval=1.0,
            profile_type="network",
        )


def test_build_profile() -> None:
    profile = build_profile(
        name="memory",
        interval=0.5,
        profile_type="memory",
        description="Memory profiler",
    )

    assert profile.name == "memory"
    assert profile.interval == 0.5
    assert profile.profile_type == "memory"
    assert profile.description == "Memory profiler"


def test_registry_register_and_get() -> None:
    registry = ProfileRegistry()

    profile = build_profile(
        name="default",
        interval=1.0,
    )

    registry.register(profile)

    assert registry.get("default") is profile
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = ProfileRegistry()

    profile = build_profile(
        name="default",
        interval=1.0,
    )

    registry.register(profile)

    with pytest.raises(DuplicateProfileError):
        registry.register(profile)


def test_registry_unregister() -> None:
    registry = ProfileRegistry()

    profile = build_profile(
        name="default",
        interval=1.0,
    )

    registry.register(profile)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = ProfileRegistry()

    with pytest.raises(ProfileNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = ProfileRegistry()

    with pytest.raises(ProfileNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = ProfileRegistry()

    registry.register(
        build_profile(
            name="one",
            interval=1.0,
        )
    )
    registry.register(
        build_profile(
            name="two",
            interval=2.0,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = ProfileRegistry()

    first = build_profile(
        name="one",
        interval=1.0,
    )
    second = build_profile(
        name="two",
        interval=2.0,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = ProfileRegistry()

    assert 123 not in registry