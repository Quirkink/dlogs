"""
Auxiliary utilities for working with directories
"""

from pathlib import Path


def get_files(paths: list[str], suffix: str = None) -> list[Path]:
    """
    Get all files from the given path.

    :param paths: Path to the file or directory.
    :param suffix: Suffix of the file.

    :return: List of Path objects.
    """

    files = []

    for path in paths:

        if Path(path).exists():
            path = Path(path)

        else:
            path = Path.cwd() / path

        if path.is_file() and (suffix is None or path.suffix == suffix):

            if path not in files:
                files.append(path)

        elif path.is_dir():

            for file in get_files(path.glob('*'), suffix):
                if file not in files:
                    files.append(file)

    return files


__all__ = (
    'get_files',
)
