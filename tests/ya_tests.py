import pytest
from main import ya_folder, ya_del_folder

token = 'my token'

FIXTURE = [
    (token, 201),
    ("no token", 401),
    (token, 409)
]

def teardown():
    ya_del_folder(token)


@pytest.mark.parametrize('token, etalon', FIXTURE)
def test_ya_folder(token, etalon):
    assert ya_folder(token) == etalon



