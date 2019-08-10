def has_sufficient_funds(cost, amount):
    return amount >= cost


def count_funds(funds):
    amount = 0

    for fund in funds:
        amount += fund['value']

    return amount
