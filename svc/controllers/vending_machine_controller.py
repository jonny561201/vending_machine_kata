from svc.services.coin import has_sufficient_funds


def controller(selection, inserted_coins):
    if not has_sufficient_funds(None, None):
        return {'message': 'Insufficient funds supplied!'}
    pass