from svc.services import coin_service


def controller(selection, inserted_coins):
    valid_coins = [valid_coin for valid_coin in inserted_coins if coin_service.is_valid_coin(valid_coin)]
    amount = coin_service.count_funds(valid_coins)
    if not coin_service.has_sufficient_funds(0.01, amount):
        return {'message': 'Insufficient funds supplied!'}, False
    return {'message': 'Thank you!'}, True
