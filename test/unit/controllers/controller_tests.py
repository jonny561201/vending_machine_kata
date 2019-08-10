from mock import patch

from svc.controllers.vending_machine_controller import controller


@patch('svc.controllers.vending_machine_controller.has_sufficient_funds')
def test_controller__should_call_has_sufficient_funds(mock_funds):
    controller(None, None)

    mock_funds.assert_called_once()
