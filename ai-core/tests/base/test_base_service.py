from base.base_service import BaseService


class DemoService(BaseService):

    def __init__(self):
        super().__init__(name="Demo Service")

    def execute(self):
        return "Service Executed"


def test_demo_service_creation():
    service = DemoService()

    assert service is not None


def test_execute():
    service = DemoService()

    assert service.execute() == "Service Executed"