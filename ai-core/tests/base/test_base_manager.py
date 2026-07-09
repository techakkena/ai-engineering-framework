from base.base_component import BaseComponent
from base.base_manager import BaseManager
import pytest

class DemoComponent(BaseComponent):
    pass


class DemoManager(BaseManager):
    pass

    @pytest.fixture
    def manager():
        return DemoManager(
            name="Framework Manager",
            description="Testing BaseManager",
        )


    @pytest.fixture
    def components():
        return [
            DemoComponent("Chat"),
            DemoComponent("RAG"),
        ]

def test_register_components():
    manager = DemoManager(
        name="Framework Manager",
        description="Testing BaseManager",
    )

    component1 = DemoComponent("Chat")
    component2 = DemoComponent("RAG")

    manager.register(component1)
    manager.register(component2)

    assert manager.count() == 2


def test_get_all():
    manager = DemoManager(
        name="Framework Manager",
        description="Testing BaseManager",
    )

    component1 = DemoComponent("Chat")
    component2 = DemoComponent("RAG")

    manager.register(component1)
    manager.register(component2)

    components = manager.get_all()

    assert len(components) == 2
    assert components[0].name == "Chat"
    assert components[1].name == "RAG"


def test_start_all():
    manager = DemoManager(
        name="Framework Manager",
        description="Testing BaseManager",
    )

    component1 = DemoComponent("Chat")
    component2 = DemoComponent("RAG")

    manager.register(component1)
    manager.register(component2)

    manager.start_all()

    assert component1.status is not None
    assert component2.status is not None


def test_stop_all():
    manager = DemoManager(
        name="Framework Manager",
        description="Testing BaseManager",
    )

    component1 = DemoComponent("Chat")
    component2 = DemoComponent("RAG")

    manager.register(component1)
    manager.register(component2)

    manager.start_all()
    manager.stop_all()

    assert component1.status is not None
    assert component2.status is not None