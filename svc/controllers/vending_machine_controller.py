from svc.services import coin


def controller(selection, inserted_coins):
    valid_coins = [valid_coin for valid_coin in inserted_coins if coin.is_valid_coin(valid_coin)]
    amount = coin.count_funds(valid_coins)
    if not coin.has_sufficient_funds(0.01, amount):
        return {'message': 'Insufficient funds supplied!'}, False
    return {'message': 'Thank you!'}, True
