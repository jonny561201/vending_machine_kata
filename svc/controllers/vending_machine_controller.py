from svc.models.coins import QUARTER
from svc.services import coin


def controller(selection, inserted_coins):
    coin.is_valid_coin(QUARTER)
    amount = coin.count_funds(inserted_coins)
    if not coin.has_sufficient_funds(0.01, amount):
        return {'message': 'Insufficient funds supplied!'}, False
    return {'message': 'Thank you!'}, True
