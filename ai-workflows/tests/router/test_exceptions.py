import pytest

from ai_workflows.router.exceptions import (
    RouteAlreadyExistsError,
    RouteNotFoundError,
)


def test_route_already_exists_error() -> None:
    with pytest.raises(RouteAlreadyExistsError):
        raise RouteAlreadyExistsError()


def test_route_not_found_error() -> None:
    with pytest.raises(RouteNotFoundError):
        raise RouteNotFoundError()
