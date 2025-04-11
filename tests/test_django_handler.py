from pathlib import Path

from dlogs.handlers.django import DjangoHandler


def test_django_handler():
    """
    Test the DjangoHandler.
    """

    handler = DjangoHandler()

    assert handler is not None


def test_django_handler_handle():
    """
    Test the DjangoHandler handle.
    """

    handler = DjangoHandler()

    data = handler.handle(
        Path(__file__).parent / 'logs' / 'django_test1.log',
    )

    assert data is not None
    assert len(data) == 5

    assert data[0][0].level == 'INFO'
    assert data[1][0].level == 'ERROR'
    assert data[2][0].level == 'DEBUG'
    assert data[3][0].level == 'WARNING'
    assert data[4][0].level == 'CRITICAL'

    assert data[0][1] == 1
    assert data[1][1] == 1
    assert data[2][1] == 1
    assert data[3][1] == 1
    assert data[4][1] == 1

    assert data[0][0].url_path == '/example/path/'
    assert data[1][0].url_path == '/example/path/'
    assert data[2][0].url_path is None
    assert data[3][0].url_path is None
    assert data[4][0].url_path is None


__all__ = (
    'test_django_handler',
    'test_django_handler_handle',
)
