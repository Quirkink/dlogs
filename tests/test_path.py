from pathlib import Path

from dlogs.utils.path import get_files


def test_get_files():
    """
    Test the get_files function.
    """

    test_path = get_files(['tests/test_path.py'])

    assert len(test_path) == 1
    assert test_path[0].name == 'test_path.py'


def test_get_multiple_files():
    """
    Test multiple files.
    """

    files = get_files([
        'tests/test_path.py',
        'tests/test_path2.py',
    ])

    assert len(files) == 1
    assert files[0].name == 'test_path.py'


def test_suffix():
    """
    Test the suffix function.
    """

    test_path = get_files(['tests'], suffix='.py')

    assert len(test_path) > 1
    assert all(path.suffix == '.py' for path in test_path)


def test_get_logs():
    """
    Test get logs.
    """

    logs = get_files([
        Path(__file__).parent / 'logs' / 'django_test1.log',
        Path(__file__).parent / 'logs' / 'django_test2.log',
    ])

    assert len(logs) == 2
    assert logs[0].name == 'django_test1.log'
    assert logs[1].name == 'django_test2.log'


__all__ = (
    'test_get_files',
    'test_get_logs',
)
