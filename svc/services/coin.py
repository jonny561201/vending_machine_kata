from svc.models.coins import QUARTER


def has_sufficient_funds(cost, amount):
    return amount >= cost


def count_funds(funds):
    amount = 0

    for fund in funds:
        amount += fund['value']

    return amount


def is_valid_coin(coin):
    if coin['weight'] == QUARTER['weight'] and coin['diameter'] == QUARTER['diameter']:
        return True
    return False
