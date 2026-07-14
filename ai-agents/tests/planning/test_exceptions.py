import pytest

from ai_agents.planning.exceptions import PlanningError


def test_planning_error() -> None:
    with pytest.raises(PlanningError):
        raise PlanningError()
