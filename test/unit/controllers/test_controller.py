from mock import patch

from svc.controllers.vending_machine_controller import controller
from svc.models.coins import DIME, QUARTER


@patch('svc.controllers.vending_machine_controller.count_funds')
@patch('svc.controllers.vending_machine_controller.has_sufficient_funds')
def test_controller__should_call_has_sufficient_funds(mock_funds, mock_count):
    controller(None, None)

    mock_funds.assert_called_once()


@patch('svc.controllers.vending_machine_controller.count_funds')
@patch('svc.controllers.vending_machine_controller.has_sufficient_funds')
def test_controller__should_call_count_funds(mock_funds, mock_count):
    controller(None, None)

    mock_count.assert_called_once()


@patch('svc.controllers.vending_machine_controller.count_funds')
@patch('svc.controllers.vending_machine_controller.has_sufficient_funds')
def test_controller__should_return_message_for_insufficient_funds(mock_funds, mock_count):
    mock_funds.return_value = False

    actual, succeeded = controller(None, None)

    assert succeeded is False
    assert actual['message'] == 'Insufficient funds supplied!'


@patch('svc.controllers.vending_machine_controller.count_funds')
@patch('svc.controllers.vending_machine_controller.has_sufficient_funds')
def test_controller__should_return_success_message_when_able_to_purchase(mock_funds, mock_count):
    mock_funds.return_value = True

    actual, succeeded = controller(None, None)

    assert succeeded is True
    assert actual['message'] == 'Thank you!'


def test_controller__should_return_success_when_using_real_services():
    funds = [QUARTER, QUARTER, DIME]
    selection = 'B10'

    actual, succeeded = controller(selection, funds)

    assert succeeded is True
    assert actual['message'] == 'Thank you!'
