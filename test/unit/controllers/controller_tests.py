from mock import patch

from svc.controllers.vending_machine_controller import controller


@patch('svc.controllers.vending_machine_controller.has_sufficient_funds')
def test_controller__should_call_has_sufficient_funds(mock_funds):
    controller(None, None)

    mock_funds.assert_called_once()


@patch('svc.controllers.vending_machine_controller.has_sufficient_funds')
def test_controller__should_return_message_for_insufficient_funds(mock_funds):
    mock_funds.return_value = False

    actual = controller(None, None)

    assert actual['message'] == 'Insufficient funds supplied!'


@patch('svc.controllers.vending_machine_controller.has_sufficient_funds')
def test_controller__should_return_success_message_when_able_to_purchase(mock_funds):
    mock_funds.return_value = True

    actual = controller(None, None)

    assert actual['message'] == 'Thank you!'
