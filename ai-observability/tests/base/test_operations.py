from ai_observability.base.constants import (
    ObservationStatus,
)
from ai_observability.base.operations import (
    BaseObserver,
    Observation,
    ObservationContext,
)


class DummyObserver(BaseObserver):
    def start(
        self,
        observation: Observation,
    ) -> None:
        observation.status = ObservationStatus.STARTED

    def stop(
        self,
        observation: Observation,
    ) -> None:
        observation.status = ObservationStatus.COMPLETED


def test_observation() -> None:
    observation = Observation(
        name="llm_call",
    )

    assert observation.name == "llm_call"

    assert observation.status is ObservationStatus.CREATED

    assert observation.attributes == {}


def test_context() -> None:
    context = ObservationContext()

    assert context.correlation_id is None

    assert context.metadata == {}


def test_dummy_observer() -> None:
    observer = DummyObserver()

    observation = Observation(
        name="test",
    )

    observer.start(observation)

    assert observation.status is ObservationStatus.STARTED

    observer.stop(observation)

    assert observation.status is ObservationStatus.COMPLETED
