from __future__ import annotations

from pathlib import Path

from utils.json_utils import JsonUtils


def test_dumps():
    data = {"name": "John", "age": 30}
    json_str = JsonUtils.dumps(data)
    assert isinstance(json_str, str)
    assert '"name": "John"' in json_str
    assert '"age": 30' in json_str


def test_loads():
    json_str = '{"name": "John", "age": 30}'
    data = JsonUtils.loads(json_str)
    assert isinstance(data, dict)
    assert data["name"] == "John"
    assert data["age"] == 30


def test_write():
    data = {"name": "John", "age": 30}
    file_path = Path("test.json")
    JsonUtils.write(file_path, data)
    assert file_path.exists()
    read_data = JsonUtils.read(file_path)
    assert read_data == data
    file_path.unlink()  # Clean up


def test_read():
    data = {"name": "John", "age": 30}
    file_path = Path("test.json")
    JsonUtils.write(file_path, data)
    read_data = JsonUtils.read(file_path)
    assert read_data == data
    file_path.unlink()  # Clean up


def test_pretty_print():
    data = {"name": "John", "age": 30}
    json_str = JsonUtils.dumps(data, indent=2)
    assert isinstance(json_str, str)
    assert json_str.startswith("{\n")
    assert json_str.endswith("\n}")
