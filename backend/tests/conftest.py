import pytest

from app import hackathon_backend_api


@pytest.fixture
def client():
    # app.app.config['TESTING'] = True
    yield hackathon_backend_api.test_client()
