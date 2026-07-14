from ai_observability.costs.operations import (
    CostRecord,
    CostRegistry,
)


def test_cost_record() -> None:
    record = CostRecord(amount=1.25)

    assert record.amount == 1.25
    assert record.currency == "USD"


def test_registry_totals() -> None:
    registry = CostRegistry()

    registry.add(CostRecord(amount=1.0))
    registry.add(CostRecord(amount=2.0))
    registry.add(CostRecord(amount=3.0))

    assert registry.count == 3
    assert registry.total_cost == 6.0
    assert registry.average_cost == 2.0


def test_empty_registry() -> None:
    registry = CostRegistry()

    assert registry.count == 0
    assert registry.total_cost == 0.0
    assert registry.average_cost == 0.0
