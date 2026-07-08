from .vector_storage import VectorStorage


class DemoVectorStorage(VectorStorage):

    def __init__(self):

        self.vectors = []

        self.metadata = []

    def add(self, vectors, metadata):

        self.vectors.extend(vectors)

        self.metadata.extend(metadata)

    def search(self, vector, k=5):

        return self.metadata[:k]

    def delete(self, ids):

        pass

    def clear(self):

        self.vectors.clear()

        self.metadata.clear()

    def count(self):

        return len(self.vectors)

    def save(self):

        print("Saved")

    def load(self):

        print("Loaded")


def main():

    storage = DemoVectorStorage()

    storage.add(
        [[0.1, 0.2, 0.3]],
        [
            {
                "text": "AI Framework",
            }
        ],
    )

    print()

    print("Count")

    print("----------------")

    print(storage.count())

    print()

    print("Search")

    print("----------------")

    print(
        storage.search(
            [0.1, 0.2, 0.3],
        )
    )

    print()

    storage.save()

    storage.load()

    print()

    storage.clear()

    print(storage.count())


if __name__ == "__main__":
    main()