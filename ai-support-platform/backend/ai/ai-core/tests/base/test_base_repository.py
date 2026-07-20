from __future__ import annotations

from base.base_repository import BaseRepository


class DemoRepository(BaseRepository):
    def __init__(self):
        super().__init__(
            name="Demo Repository",
            description="Testing BaseRepository",
        )
        self.records = {}

    def create(self, data):
        record_id = len(self.records) + 1
        self.records[record_id] = data
        return record_id

    def get_by_id(self, record_id):
        return self.records.get(record_id)

    def get_all(self):
        return self.records

    def update(self, record_id, data):
        self.records[record_id] = data

    def delete(self, record_id):
        self.records.pop(record_id, None)

    def exists(self, record_id):
        return record_id in self.records

    def count(self):
        return len(self.records)


def test_demo_repository_creation():
    repo = DemoRepository()

    assert repo is not None
    assert repo.name == "Demo Repository"
    assert repo.description == "Testing BaseRepository"
    assert repo.count() == 0


def test_create():
    repo = DemoRepository()

    record_id = repo.create({"name": "John"})

    assert record_id == 1
    assert repo.count() == 1


def test_get_by_id():
    repo = DemoRepository()

    record_id = repo.create({"name": "John"})

    record = repo.get_by_id(record_id)

    assert record == {"name": "John"}


def test_get_all():
    repo = DemoRepository()

    repo.create({"name": "John"})
    repo.create({"name": "Alice"})

    records = repo.get_all()

    assert len(records) == 2


def test_update():
    repo = DemoRepository()

    record_id = repo.create({"name": "John"})

    repo.update(record_id, {"name": "Alice"})

    assert repo.get_by_id(record_id) == {"name": "Alice"}


def test_exists():
    repo = DemoRepository()

    record_id = repo.create({"name": "John"})

    assert repo.exists(record_id) is True
    assert repo.exists(999) is False


def test_delete():
    repo = DemoRepository()

    record_id = repo.create({"name": "John"})

    repo.delete(record_id)

    assert repo.count() == 0
    assert repo.exists(record_id) is False


def test_count():
    repo = DemoRepository()

    repo.create({"name": "John"})
    repo.create({"name": "Alice"})

    assert repo.count() == 2
