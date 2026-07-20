from __future__ import annotations

from base.base_controller import BaseController


class DemoController(BaseController):
    def execute(self):
        return self.success(data={"framework": "AI Engineering Framework"})


def test_demo_controller_creation():
    controller = DemoController(
        name="Demo Controller",
        description="Testing BaseController",
    )

    assert controller is not None
    assert controller.name == "Demo Controller"
    assert controller.description == "Testing BaseController"


def test_execute():
    controller = DemoController(
        name="Demo Controller",
        description="Testing BaseController",
    )

    result = controller.execute()

    assert result is not None
    assert result["success"] is True
    assert result["data"]["framework"] == "AI Engineering Framework"


def test_error():
    controller = DemoController(
        name="Demo Controller",
        description="Testing BaseController",
    )

    result = controller.error(
        "Validation failed.",
        {"field": "email"},
    )

    assert result is not None
    assert result["success"] is False
    assert result["message"] == "Validation failed."
    assert result["details"]["field"] == "email"


def test_initialize():
    controller = DemoController(
        name="Demo Controller",
        description="Testing BaseController",
    )

    controller.initialize()

    assert controller.status is not None
