from svc.models.coins import QUARTER
from svc.services.coin import has_sufficient_funds, count_funds, is_valid_coin


def controller(selection, inserted_coins):
    is_valid_coin(QUARTER)
    amount = count_funds(inserted_coins)
    if not has_sufficient_funds(0.01, amount):
        return {'message': 'Insufficient funds supplied!'}, False
    return {'message': 'Thank you!'}, True
