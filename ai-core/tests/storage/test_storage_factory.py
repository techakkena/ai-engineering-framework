from storage.storage_factory import StorageFactory
from constants.storage_constants import StorageTypes
from storage.file_storage import FileStorage

def test_create_local_storage():
    storage = StorageFactory.create(StorageTypes.LOCAL)

    assert isinstance(storage, FileStorage)
