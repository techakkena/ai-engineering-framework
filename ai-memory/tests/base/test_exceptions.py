"""Tests for ai_memory.base.exceptions."""

from ai_memory.base.exceptions import MemoryCapacityError
from ai_memory.base.exceptions import MemoryConfigurationError
from ai_memory.base.exceptions import MemoryError
from ai_memory.base.exceptions import MemoryNotFoundError
from ai_memory.base.exceptions import MemorySerializationError
from ai_memory.base.exceptions import MemoryStorageError
from ai_memory.base.exceptions import MemoryValidationError


def test_memory_error_inheritance() -> None:
    """Test exception inheritance."""
    assert issubclass(MemoryValidationError, MemoryError)
    assert issubclass(MemoryNotFoundError, MemoryError)
    assert issubclass(MemoryStorageError, MemoryError)
    assert issubclass(MemorySerializationError, MemoryError)
    assert issubclass(MemoryConfigurationError, MemoryError)
    assert issubclass(MemoryCapacityError, MemoryError)


def test_raise_memory_validation_error() -> None:
    """Test raising MemoryValidationError."""
    try:
        raise MemoryValidationError("invalid")
    except MemoryValidationError as exc:
        assert str(exc) == "invalid"


def test_raise_memory_not_found_error() -> None:
    """Test raising MemoryNotFoundError."""
    try:
        raise MemoryNotFoundError("missing")
    except MemoryNotFoundError as exc:
        assert str(exc) == "missing"


def test_raise_memory_storage_error() -> None:
    """Test raising MemoryStorageError."""
    try:
        raise MemoryStorageError("storage")
    except MemoryStorageError as exc:
        assert str(exc) == "storage"


def test_raise_memory_serialization_error() -> None:
    """Test raising MemorySerializationError."""
    try:
        raise MemorySerializationError("serialization")
    except MemorySerializationError as exc:
        assert str(exc) == "serialization"


def test_raise_memory_configuration_error() -> None:
    """Test raising MemoryConfigurationError."""
    try:
        raise MemoryConfigurationError("configuration")
    except MemoryConfigurationError as exc:
        assert str(exc) == "configuration"


def test_raise_memory_capacity_error() -> None:
    """Test raising MemoryCapacityError."""
    try:
        raise MemoryCapacityError("capacity")
    except MemoryCapacityError as exc:
        assert str(exc) == "capacity"
