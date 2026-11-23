import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def create_file(file_path):
    path = Path(file_path)

    if not path.is_absolute():
        raise ValueError("Please provide an absolute file path.")

    if path.exists():
        raise FileExistsError("File already exists.")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("", encoding="utf-8")

    logger.info("Created file: %s", path)

    return path


def read_file(file_path):
    path = Path(file_path)

    if not path.is_absolute():
        raise ValueError("Please provide an absolute file path.")

    if not path.is_file():
        raise FileNotFoundError("File does not exist.")

    content = path.read_text(encoding="utf-8")

    logger.info("Opened file: %s", path)

    return content


def save_file(file_path, content):
    path = Path(file_path)

    if not path.is_absolute():
        raise ValueError("Please provide an absolute file path.")

    if not path.is_file():
        raise FileNotFoundError("File does not exist.")

    path.write_text(content, encoding="utf-8")

    logger.info("Saved file: %s", path)

    return path
