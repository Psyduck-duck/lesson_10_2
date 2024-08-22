import pytest
from src.task1 import calculate_taxes


@pytest.mark.parametrize("tax_rate, expected", [(10, [110, 220, 330]),
                                                (15, [115, 230, 345]),
                                                (20, [120, 240, 360])])
def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected

def test_calculate_invalid_taxes(prices):
    with pytest.raises(ValueError):

        calculate_taxes([1, 2, 3], -1)


def test_calculate_invalid_prices():
    with pytest.raises(ValueError):
        calculate_taxes([-1, -2], 0)
