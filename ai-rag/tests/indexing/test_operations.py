from ai_rag.indexing.operations import (
    default_batch_size,
    default_index_name,
    validate_batch_size,
    validate_index_name,
)


def test_default_index_name():
    assert default_index_name() == "default"


def test_default_batch_size():
    assert default_batch_size() == 100


def test_valid_index_name():
    assert validate_index_name("knowledge-base")


def test_invalid_index_name():
    assert not validate_index_name("")


def test_valid_batch_size():
    assert validate_batch_size(500)


def test_invalid_batch_size_low():
    assert not validate_batch_size(0)


def test_invalid_batch_size_high():
    assert not validate_batch_size(50000)