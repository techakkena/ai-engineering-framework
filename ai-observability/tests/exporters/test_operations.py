from ai_observability.exporters.operations import (
    ExportRecord,
    MemoryExporter,
)


def test_export_record() -> None:
    exporter = MemoryExporter()

    exporter.export(
        ExportRecord(
            name="trace",
            payload={"id": "trace-1"},
        )
    )

    assert exporter.count == 1
    assert exporter.records[0].name == "trace"


def test_clear_records() -> None:
    exporter = MemoryExporter()

    exporter.export(
        ExportRecord(
            name="metric",
            payload={"value": 1},
        )
    )

    exporter.clear()

    assert exporter.count == 0
