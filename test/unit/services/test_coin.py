from svc.services.coin import has_sufficient_funds


def test_has_sufficient_funds__should_return_true_when_enough_funds_supplied():
    cost = 1.00
    amount = 1.25

    actual = has_sufficient_funds(cost, amount)

    assert actual is True


def test_has_sufficient_funds__should_return_false_when_more_than_enough_funds_supplied():
    cost = 0.75
    amount = 0.50

    actual = has_sufficient_funds(cost, amount)

    assert actual is False
