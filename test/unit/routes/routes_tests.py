import json

from mock import patch

from svc.routes.routes import health_status, purchase


def test_health_status__should_return_success():
    actual = health_status()

    assert actual == 'Success'


@patch('svc.routes.routes.controller')
def test_purchase__should_return_response_from_controller(mock_controller):
    message = 'Nice Job'
    mock_controller.return_value = {'message': message}

    actual = purchase()
    json_actual = json.loads(actual)

    assert json_actual['message'] == message
