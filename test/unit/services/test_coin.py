from svc.models.coins import NICKEL, QUARTER, DIME, DOLLAR
from svc.services.coin import has_sufficient_funds, count_funds, is_valid_coin


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


def test_has_sufficient_funds__should_return_true_when_cost_equal_amount():
    cost = 0.75
    amount = 0.75

    actual = has_sufficient_funds(cost, amount)

    assert actual is True


def test_count_funds__should_return_value_for_single_coin():
    funds = [NICKEL]

    actual = count_funds(funds)

    assert actual == 0.05


def test_count_funds__should_return_value_for_multiple_coins():
    funds = [NICKEL, NICKEL]

    actual = count_funds(funds)

    assert actual == 0.10


def test_count_funds__should_return_zero_when_no_funds():
    funds = []

    actual = count_funds(funds)

    assert actual == 0.00


def test_is_valid_coin__should_return_true_when_quarter_supplied():
    actual = is_valid_coin(QUARTER)

    assert actual is True


def test_is_valid_coin__should_return_true_when_nickel_supplied():
    actual = is_valid_coin(NICKEL)

    assert actual is True


def test_is_valid_coin__should_return_true_when_dime_supplied():
    actual = is_valid_coin(DIME)

    assert actual is True


def test_is_valid_coin__should_return_true_when_dollar_supplied():
    actual = is_valid_coin(DOLLAR)

    assert actual is True


def test_is_valid_coin__should_return_false_when_invalid_weight_coin_supplied():
    invalid_coin = {'weight': 56.99}
    actual = is_valid_coin(invalid_coin)

    assert actual is False


def test_is_valid_coin__should_return_false_when_invalid_diameter_coin_supplied():
    invalid_coin = {'diameter': 42.76, 'weight': QUARTER['weight']}
    actual = is_valid_coin(invalid_coin)

    assert actual is False
