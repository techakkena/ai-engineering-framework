from pathlib import Path

from utils.path_utils import PathUtils

def test_exists():
    path = Path("test_dir")
    PathUtils.create_directory(path)
    assert PathUtils.exists(path) is True
    PathUtils.delete(path)
    assert PathUtils.exists(path) is False

def test_create_directory():    
    path = Path("test_dir")
    PathUtils.create_directory(path)
    assert path.exists() is True
    PathUtils.delete(path)  

def test_ensure_directory():
    path = Path("test_dir/test_file.txt")
    PathUtils.ensure_directory(path)
    assert path.parent.exists() is True
    PathUtils.delete(path.parent)

def test_delete():
    path = Path("test_dir")
    PathUtils.create_directory(path)
    assert PathUtils.delete(path) is True
    assert path.exists() is False

def test_file_name():
    path = Path("test_dir/test_file.txt")
    PathUtils.ensure_directory(path)
    assert PathUtils.file_name(path) == "test_file.txt"
    PathUtils.delete(path.parent)

def test_extension():
    path = Path("test_dir/test_file.txt")
    PathUtils.ensure_directory(path)
    assert path.suffix == ".txt"
    PathUtils.delete(path.parent)

def test_parent():
    path = Path("test_dir/test_file.txt")
    PathUtils.ensure_directory(path)
    assert PathUtils.parent(path) == path.parent
    PathUtils.delete(path.parent)

def test_resolve():
    path = Path("test_dir/test_file.txt")
    PathUtils.ensure_directory(path)
    assert PathUtils.resolve(path) == path.resolve()
    PathUtils.delete(path.parent)

def test_join():
    path1 = Path("test_dir")
    path2 = Path("test_file.txt")
    joined_path = PathUtils.join(path1, path2)
    assert joined_path == path1 / path2
