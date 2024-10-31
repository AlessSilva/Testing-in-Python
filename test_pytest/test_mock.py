import requests


def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()


def test_get_user_data(mocker):
    mock_response_data = {'name': 'John', 'email': 'john@example.com'}

    mock_get = mocker.patch('requests.get')
    mock_get.return_value.json.return_value = mock_response_data

    user_data = get_user_data(1)

    mock_get.assert_called_once_with("https://api.example.com/users/1")

    assert user_data == mock_response_data
