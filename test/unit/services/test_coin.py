from svc.services.coin import has_sufficient_funds


def test_has_sufficient_funds__should_return_true_when_enough_funds_supplied():
    cost = 1.00
    amount = 0.75

    actual = has_sufficient_funds(cost, amount)

    assert actual is True