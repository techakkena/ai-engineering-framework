from .base_repository import BaseRepository


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


def main():

    repo = DemoRepository()

    repo.initialize()

    record_id = repo.create({"name": "John"})

    print()

    print("Count")
    print("----------------")

    print(repo.count())

    print()

    print("Record")
    print("----------------")

    print(repo.get_by_id(record_id))

    print()

    print("Exists")
    print("----------------")

    print(repo.exists(record_id))

    print()

    repo.update(record_id, {"name": "Alice"})

    print(repo.get_by_id(record_id))

    print()

    repo.delete(record_id)

    print("Count :", repo.count())


if __name__ == "__main__":
    main()