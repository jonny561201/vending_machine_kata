from svc.services import coin_service
from svc.services.product_service import ProductService


def controller(selection, inserted_coins):
    product_service = ProductService(None)
    if not product_service.is_product_available(selection):
        return {'message': 'Product is unavailable!'}, False
    valid_coins = [valid_coin for valid_coin in inserted_coins if coin_service.is_valid_coin(valid_coin)]
    amount = coin_service.count_funds(valid_coins)
    product_service.get_product_cost(None)
    if not coin_service.has_sufficient_funds(0.01, amount):
        return {'message': 'Insufficient funds supplied!'}, False
    return {'message': 'Thank you!'}, True
