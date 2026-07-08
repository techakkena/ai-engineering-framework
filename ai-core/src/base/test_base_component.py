from .base_component import BaseComponent


class DemoComponent(BaseComponent):

    pass


def main():

    component = DemoComponent(
        name="AI Core",
        description="Framework Core Component",
    )

    print()

    print("Information")

    print("---------------------")

    print(component.get_info())

    print()

    component.initialize()

    print("Health")

    print("---------------------")

    print(component.health_check())

    print()

    print("Dictionary")

    print("---------------------")

    print(component.to_dict())

    print()

    component.shutdown()

    print(component.status)


if __name__ == "__main__":
    main()