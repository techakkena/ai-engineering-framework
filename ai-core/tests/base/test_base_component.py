import pytest

from base.base_component import BaseComponent


class DemoComponent(BaseComponent):
    pass


@pytest.fixture
def component():
    return DemoComponent(
        name="AI Core",
        description="Framework Core Component",
    )


def test_component_creation(component):
    assert component is not None
    assert component.name == "AI Core"
    assert component.description == "Framework Core Component"


def test_get_info(component):
    info = component.get_info()

    assert info is not None


def test_health_check(component):
    health = component.health_check()

    assert health is not None


def test_to_dict(component):
    data = component.to_dict()

    assert isinstance(data, dict)


def test_initialize(component):
    component.initialize()

    assert component.status is not None


def test_shutdown(component):
    component.shutdown()

    assert component.status is not None
