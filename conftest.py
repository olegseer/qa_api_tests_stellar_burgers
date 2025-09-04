import pytest

from generators import generate_user_body


@pytest.fixture
def user_data():
    create_body = generate_user_body()
    yield create_body
