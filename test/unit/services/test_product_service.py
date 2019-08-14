from mock import patch

from svc.services.product_service import is_product_available


@patch('svc.services.product_service.get_product_by_location')
def test_is_product_available__should_return_true_when_product_is_returned(mock_database):
    product = {'name': 'twix'}
    mock_database.return_value = [product]
    selection = 'A1'
    actual = is_product_available(selection)

    assert actual is True

