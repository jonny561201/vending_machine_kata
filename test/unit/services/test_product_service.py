from mock import patch

from svc.services.product_service import is_product_available, get_product_cost


@patch('svc.services.product_service.get_product_by_location')
def test_is_product_available__should_return_true_when_product_is_returned(mock_database):
    product = {'name': 'twix'}
    mock_database.return_value = [product]
    selection = 'A1'
    actual = is_product_available(selection)

    assert actual is True


@patch('svc.services.product_service.get_product_by_location')
def test_is_product_available__should_return_false_when_products_are_empty(mock_database):
    mock_database.return_value = []
    selection = 'A1'
    actual = is_product_available(selection)

    assert actual is False


@patch('svc.services.product_service.get_product_by_location')
def test_get_product_cost__should_return_cost(mock_database):
    cost = 0.75
    product = {'cost': cost}
    selection = 'B10'
    mock_database.return_value = [product]

    actual = get_product_cost(selection)

    assert actual == cost


@patch('svc.services.product_service.get_product_by_location')
def test_get_product_cost__should_return_zero_when_no_product(mock_database):
    selection = 'B10'
    mock_database.return_value = []

    actual = get_product_cost(selection)

    assert actual == 0.00
