from ai_agents.planning.operations import (
    Plan,
    PlanStep,
    SimplePlanner,
)


def test_plan_step() -> None:
    step = PlanStep(
        id=1,
        description="Search documentation",
    )

    assert step.id == 1
    assert step.description == "Search documentation"


def test_plan_add_step() -> None:
    plan = Plan()

    plan.add_step(
        PlanStep(
            id=1,
            description="Task",
        )
    )

    assert plan.size == 1


def test_create_plan() -> None:
    planner = SimplePlanner()

    plan = planner.create_plan(
        "Build API",
    )

    assert plan.size == 1
    assert plan.steps[0].description == "Build API"


def test_empty_plan() -> None:
    plan = Plan()

    assert plan.size == 0
