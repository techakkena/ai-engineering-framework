from __future__ import annotations

from pathlib import Path

from utils.file_utils import FileUtils


def test_read_text(tmp_path: Path):
    test_file = tmp_path / "test.txt"
    test_content = "Hello, World!"
    test_file.write_text(test_content)

    content = FileUtils.read_text(test_file)

    assert content == test_content


def test_write_text(tmp_path: Path):
    test_file = tmp_path / "test.txt"
    test_content = "Hello, World!"

    FileUtils.write_text(test_file, test_content)

    assert test_file.read_text() == test_content


def test_copy(tmp_path: Path):
    source_file = tmp_path / "source.txt"
    destination_file = tmp_path / "destination.txt"
    test_content = "Hello, World!"
    source_file.write_text(test_content)

    FileUtils.copy(source_file, destination_file)

    assert destination_file.read_text() == test_content


def test_move(tmp_path: Path):
    source_file = tmp_path / "source.txt"
    destination_file = tmp_path / "destination.txt"
    test_content = "Hello, World!"
    source_file.write_text(test_content)

    FileUtils.move(source_file, destination_file)

    assert destination_file.read_text() == test_content
    assert not source_file.exists()


def test_rename():
    source_file = Path("source.txt")
    destination_file = Path("destination.txt")
    test_content = "Hello, World!"
    source_file.write_text(test_content)

    FileUtils.move(source_file, destination_file)

    assert destination_file.read_text() == test_content
    assert not source_file.exists()


def test_size():
    test_file = Path("test.txt")
    test_content = "Hello, World!"
    test_file.write_text(test_content)

    size = FileUtils.size(test_file)

    assert size == len(test_content)


def test_delete():
    test_file = Path("test.txt")
    test_content = "Hello, World!"
    test_file.write_text(test_content)

    FileUtils.delete(test_file)

    assert not test_file.exists()
