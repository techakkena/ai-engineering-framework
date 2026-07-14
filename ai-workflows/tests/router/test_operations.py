import pytest

from ai_workflows.router.exceptions import (
    RouteAlreadyExistsError,
    RouteNotFoundError,
)
from ai_workflows.router.operations import Router


def test_register_route() -> None:
    router = Router()

    router.register(
        "success",
        "pipeline_a",
    )

    assert router.size == 1


def test_duplicate_route() -> None:
    router = Router()

    router.register(
        "success",
        "pipeline_a",
    )

    with pytest.raises(RouteAlreadyExistsError):
        router.register(
            "success",
            "pipeline_b",
        )


def test_resolve_route() -> None:
    router = Router()

    router.register(
        "success",
        "pipeline_a",
    )

    assert router.resolve("success") == "pipeline_a"


def test_missing_route() -> None:
    router = Router()

    with pytest.raises(RouteNotFoundError):
        router.resolve("missing")


def test_remove_route() -> None:
    router = Router()

    router.register(
        "success",
        "pipeline_a",
    )

    router.remove("success")

    assert router.size == 0


def test_clear_routes() -> None:
    router = Router()

    router.register("a", "pipeline1")
    router.register("b", "pipeline2")

    router.clear()

    assert router.size == 0


def test_exists() -> None:
    router = Router()

    router.register(
        "success",
        "pipeline",
    )

    assert router.exists("success")
    assert not router.exists("failure")
