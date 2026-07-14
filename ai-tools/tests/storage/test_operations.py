from ai_tools.storage.operations import (
    StorageClient,
    StorageObject,
)


def test_put_object() -> None:
    client = StorageClient()

    obj = StorageObject(
        key="file.txt",
        data=b"hello",
    )

    client.put(obj)

    assert client.object_count == 1


def test_get_object() -> None:
    client = StorageClient()

    obj = StorageObject(
        key="file.txt",
        data=b"hello",
    )

    client.put(obj)

    result = client.get("file.txt")

    assert result is obj


def test_exists() -> None:
    client = StorageClient()

    client.put(
        StorageObject(
            key="file.txt",
            data=b"hello",
        )
    )

    assert client.exists("file.txt")
    assert not client.exists("missing")


def test_delete_object() -> None:
    client = StorageClient()

    client.put(
        StorageObject(
            key="file.txt",
            data=b"hello",
        )
    )

    client.delete("file.txt")

    assert client.object_count == 0
    assert client.get("file.txt") is None
