from svc.models.coins import VALID_COINS


def has_sufficient_funds(cost, amount):
    return amount >= cost


def count_funds(funds):
    amount = 0

    for fund in funds:
        amount += fund['value']

    return amount


def is_valid_coin(coin):
    for valid_coin in VALID_COINS:
        if coin['weight'] == valid_coin['weight'] and coin['diameter'] == valid_coin['diameter']:
            return True
    return False
