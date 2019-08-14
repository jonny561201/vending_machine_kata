from mock import patch, mock

from svc.repositories import product_database
from svc.services.product_service import ProductService


class TestProductService:
    def setup_method(self):
        self.mock_database = mock.create_autospec(product_database)

    def test_is_product_available__should_return_true_when_product_is_returned(self):
        product_service = ProductService(self.mock_database)
        product = {'name': 'twix'}
        self.mock_database.get_product_by_location.return_value = [product]
        selection = 'A1'
        actual = product_service.is_product_available(selection)

        assert actual is True

    def test_is_product_available__should_return_false_when_products_are_empty(self):
        product_service = ProductService(self.mock_database)
        self.mock_database.get_product_by_location.return_value = []
        selection = 'A1'
        actual = product_service.is_product_available(selection)

        assert actual is False

    def test_get_product_cost__should_return_cost(self):
        product_service = ProductService(self.mock_database)
        cost = 0.75
        product = {'cost': cost}
        selection = 'B10'
        self.mock_database.get_product_by_location.return_value = [product]

        actual = product_service.get_product_cost(selection)

        assert actual == cost

    def test_get_product_cost__should_return_zero_when_no_product(self):
        product_service = ProductService(self.mock_database)
        selection = 'B10'
        self.mock_database.get_product_by_location.return_value = []

        actual = product_service.get_product_cost(selection)

        assert actual == 0.00

    def test_get_product_cost__should_cache_product_when_product_queried(self):
        selection = 'B10'
        product = {'cost': 0.35}
        product_service = ProductService(self.mock_database)
        self.mock_database.get_product_by_location.return_value = [product]

        product_service.is_product_available(selection)
        product_service.get_product_cost(selection)

        assert product_service.products == [product]
        assert self.mock_database.get_product_by_location.call_count == 1
