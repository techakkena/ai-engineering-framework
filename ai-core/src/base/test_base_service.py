from .base_service import BaseService


class DemoService(BaseService):

    def execute(self):

        return "Service Executed"


def main():

    service = DemoService(
        name="Demo Service",
        description="Testing BaseService",
    )

    print("\nService Information")
    print("--------------------")
    print(service.get_info())

    print("\nInitialize")
    print("--------------------")
    service.initialize()
    print(service.status)

    print("\nStart")
    print("--------------------")
    service.start()
    print(service.status)

    print("\nRunning")
    print("--------------------")
    print(service.is_running())

    print("\nExecute")
    print("--------------------")
    print(service.execute())

    print("\nRestart")
    print("--------------------")
    service.restart()
    print(service.status)

    print("\nStop")
    print("--------------------")
    service.stop()
    print(service.status)

if __name__ == "__main__":
    main()