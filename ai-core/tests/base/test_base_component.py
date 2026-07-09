from base.base_component import BaseComponent
import pytest


class DemoComponent(BaseComponent):

    pass

    @pytest.fixture
    def component():
        return DemoComponent(
            name="AI Core",
            description="Framework Core Component",
        )

        assert component is not None
        assert component.name == "AI Core"
        assert component.description == "Framework Core Component"


def test_get_info():
    component = DemoComponent(
        name="AI Core",
        description="Framework Core Component",
    )

    info = component.get_info()

    assert info is not None


def test_health_check():
    component = DemoComponent(
        name="AI Core",
        description="Framework Core Component",
    )

    health = component.health_check()

    assert health is not None


def test_to_dict():
    component = DemoComponent(
        name="AI Core",
        description="Framework Core Component",
    )

    data = component.to_dict()

    assert isinstance(data, dict)


def test_initialize():
    component = DemoComponent(
        name="AI Core",
        description="Framework Core Component",
    )

    component.initialize()

    assert component.status is not None


def test_shutdown():
    component = DemoComponent(
        name="AI Core",
        description="Framework Core Component",
    )

    component.shutdown()

    assert component.status is not None