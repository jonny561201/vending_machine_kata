from svc.services.coin import has_sufficient_funds, count_funds


def controller(selection, inserted_coins):
    amount = count_funds(inserted_coins)
    if not has_sufficient_funds(0.01, amount):
        return {'message': 'Insufficient funds supplied!'}, False
    return {'message': 'Thank you!'}, True
