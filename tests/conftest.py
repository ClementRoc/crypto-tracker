import pytest

from cryptoapp import app
from cryptoapp.database import init_db


@pytest.fixture
def app(app=app):
    with app.app_context():
        init_db()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

