from pathlib import Path

from utils.hash_utils import HashUtils
from utils.file_utils import FileUtils

def test_md5():
    data = "Hello, World!"
    expected_hash = "65a8e27d8879283831b664bd8b7f0ad4"
    assert HashUtils.md5(data) == expected_hash

def test_sha1():
    data = "Hello, World!"
    expected_hash = "0a0a9f2a6772942557ab5355d76af442f8f65e01"

    assert HashUtils.sha1(data) == expected_hash

def test_sha256():
    data = "Hello, World!"
    expected_hash = (
    "dffd6021bb2bd5b0af676290809ec3a53191dd81"
    "c7f70a4b28688a362182986f"
    )

def test_sha512():
    data = "Hello, World!"
    expected_hash = "861844d6704e8573fec34d967e20bcfe6f0a1f7c9b8b6f5c1e"

def test_file_sha256(tmp_path: Path):
    test_file = tmp_path / "test.txt"
    test_content = "Hello, World!"
    test_file.write_text(test_content)

    expected_hash = "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"
    assert HashUtils.file_sha256(test_file) == expected_hash

def test_verify_file_sha256(tmp_path: Path):
    test_file = tmp_path / "test.txt"
    test_content = "Hello, World!"
    test_file.write_text(test_content)

    expected_hash = "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"
    assert HashUtils.verify_sha256(test_content, expected_hash) is True

