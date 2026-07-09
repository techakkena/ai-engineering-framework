from storage.cache_manager import CacheManager

def test_cache_manager_init():
    cache_manager = CacheManager()

    assert cache_manager is not None
    assert cache_manager.cache_dir is not None

def test_set():
    cache_manager = CacheManager()

    # Set a value in the cache
    key = "test_key"
    value = {"name": "John", "age": 30}
    result = cache_manager.set(key, value)

    assert result is True

def test_get():
    cache_manager = CacheManager()

    # Set a value in the cache
    key = "test_key"

    value = {"name": "John", "age": 30}
    cache_manager.set(key, value)

    # Get the value from the cache
    retrieved_value = cache_manager.get(key)

    assert retrieved_value == value

def test_exists():
    cache_manager = CacheManager()

    # Set a value in the cache
    key = "test_key"
    value = {"name": "John", "age": 30} 
    cache_manager.set(key, value)
    
    # Check if the cache file exists
    file_path = cache_manager._cache_file(key)
    assert cache_manager.exists(key) is True
    assert file_path.exists() is True

def test_delete():
    cache_manager = CacheManager()

    # Set a value in the cache
    key = "test_key"    
    value = {"name": "John", "age": 30}
    cache_manager.set(key, value)   
    cache_manager.delete(key)
    assert cache_manager.exists(key) is False

def test_clear():
    cache_manager = CacheManager()

    # Set multiple values in the cache
    cache_manager.set("key1", {"name": "John"})
    cache_manager.set("key2", {"name": "Alice"})

    # Clear the cache
    cache_manager.clear()

    # Check if the cache files are deleted
    assert cache_manager.exists("key1") is False
    assert cache_manager.exists("key2") is False

