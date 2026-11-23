import subprocess

import pytest

from app import git_manager


def test_commit_file(tmp_path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("First version", encoding="utf-8")

    first_commit = git_manager.commit_file(file_path)

    assert first_commit is True

    second_commit = git_manager.commit_file(file_path)

    assert second_commit is False

    file_path.write_text("Updated version", encoding="utf-8")

    third_commit = git_manager.commit_file(file_path)

    assert third_commit is True

    result = subprocess.run(
        ["git", "log", "--oneline"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=True
    )

    commits = result.stdout.strip().splitlines()

    assert len(commits) == 2


def test_commit_nonexistent_file(tmp_path):
    file_path = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        git_manager.commit_file(file_path)
