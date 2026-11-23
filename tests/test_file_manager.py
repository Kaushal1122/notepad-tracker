import pytest

from app import file_manager


def test_create_file(tmp_path):
    file_path = tmp_path / "notes" / "test.txt"

    result = file_manager.create_file(file_path)

    assert result == file_path
    assert file_path.exists()
    assert file_path.read_text(encoding="utf-8") == ""


def test_create_file_requires_absolute_path():
    with pytest.raises(ValueError):
        file_manager.create_file("notes.txt")


def test_create_existing_file(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("Existing content", encoding="utf-8")

    with pytest.raises(FileExistsError):
        file_manager.create_file(file_path)


def test_read_file(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("Hello World", encoding="utf-8")

    content = file_manager.read_file(file_path)

    assert content == "Hello World"


def test_read_nonexistent_file(tmp_path):
    file_path = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        file_manager.read_file(file_path)


def test_save_file(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("Old content", encoding="utf-8")

    result = file_manager.save_file(file_path, "New content")

    assert result == file_path
    assert file_path.read_text(encoding="utf-8") == "New content"


def test_save_nonexistent_file(tmp_path):
    file_path = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        file_manager.save_file(file_path, "Content")
