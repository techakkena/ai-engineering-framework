from .base_component import BaseComponent
from .base_manager import BaseManager


class DemoComponent(BaseComponent):

    pass


class DemoManager(BaseManager):

    pass


def main():

    manager = DemoManager(
        name="Framework Manager",
        description="Testing BaseManager",
    )

    component1 = DemoComponent("Chat")

    component2 = DemoComponent("RAG")

    manager.register(component1)

    manager.register(component2)

    print()

    print("Count")

    print("----------------")

    print(manager.count())

    print()

    print("Components")

    print("----------------")

    for component in manager.get_all():

        print(component.name)

    print()

    manager.start_all()

    print(component1.status)

    print(component2.status)

    print()

    manager.stop_all()

    print(component1.status)

    print(component2.status)


if __name__ == "__main__":
    main()