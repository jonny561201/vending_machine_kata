from mock import patch

from svc.controllers.vending_machine_controller import controller


@patch('svc.controllers.vending_machine_controller.has_sufficient_funds')
def test_controller__should_call_has_sufficient_funds(mock_funds):
    inserted_coins = []
    selection = 'H3'
    mock_funds.return_value = False

    controller(selection, inserted_coins)

    mock_funds.assert_called_once()