from .base_controller import BaseController


class DemoController(BaseController):

    def execute(self):

        return self.success(
            data={
                "framework": "AI Engineering Framework"
            }
        )


def main():

    controller = DemoController(
        name="Demo Controller",
        description="Testing BaseController",
    )

    controller.initialize()

    print()

    print(controller.execute())

    print()

    print(
        controller.error(
            "Validation failed.",
            {"field": "email"},
        )
    )


if __name__ == "__main__":
    main()