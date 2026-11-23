import logging
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)


def run_git_command(command, directory):
    return subprocess.run(
        ["git", *command],
        cwd=directory,
        capture_output=True,
        text=True,
        check=True
    )


def commit_file(file_path):
    path = Path(file_path).resolve()

    if not path.is_file():
        raise FileNotFoundError("File does not exist.")

    try:
        result = run_git_command(
            ["rev-parse", "--show-toplevel"],
            path.parent
        )

        repository = Path(result.stdout.strip()).resolve()

    except subprocess.CalledProcessError:
        run_git_command(["init"], path.parent)
        repository = path.parent

        logger.info("Initialized Git repository: %s", repository)

    relative_path = path.relative_to(repository)

    run_git_command(
        ["add", "--", str(relative_path)],
        repository
    )

    result = subprocess.run(
        [
            "git",
            "diff",
            "--cached",
            "--quiet",
            "--",
            str(relative_path)
        ],
        cwd=repository,
        capture_output=True,
        text=True,
        check=False
    )

    if result.returncode == 0:
        logger.info("No changes to commit: %s", path)
        return False

    if result.returncode != 1:
        raise RuntimeError(
            result.stderr or "Unable to check Git changes."
        )

    run_git_command(
        [
            "commit",
            "-m",
            f"Update {path.name}",
            "--only",
            "--",
            str(relative_path)
        ],
        repository
    )

    logger.info("Created Git commit for: %s", path)

    return True
