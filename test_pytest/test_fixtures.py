import pytest


@pytest.fixture
def sample_data():
    return [1, 2, 3, 4]


@pytest.fixture(autouse=True)
def setup_login():
    print("Setup login")


def test_sample_data(sample_data):
    assert sum(sample_data) == 10


@pytest.fixture
def user():
    return {"id": 1, 'username': "Test user"}


@pytest.fixture
def user_with_friends(user):
    user['friends'] = ['Friend 1', 'Friend 2']
    return user


def test_user_data(user_with_friends):
    assert len(user_with_friends['friends']) == 2


@pytest.fixture
def custom_list(request):
    length = request.param
    return [0] * length


@pytest.mark.parametrize("custom_list", [2, 4], indirect=True)
def test_list(custom_list):
    assert len(custom_list) % 2 == 0


@pytest.fixture
def temporary_file():
    file = open("temp.txt", "w")
    yield file
    file.close()
