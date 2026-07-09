from storage.vector_storage import VectorStorage


def test_vector_storage_is_abstract():  
    """
    VectorStorage is an abstract class and cannot be instantiated.
    """
    try:
        VectorStorage()
        assert False, "VectorStorage should not be instantiable"
    except TypeError:
        pass  # Expected behavior

        
