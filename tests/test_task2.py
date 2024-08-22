import pytest
from src.task2 import calculate_tax


@pytest.mark.parametrize('price, tax_rate, expected', [(100, 10, 110),
                                                      (200, 30, 260),
                                                      (300, 10, 330),
                                                      (100, 20, 120)])

def test_calculate_tax(price, tax_rate, expected):
    calculate_tax(price, tax_rate) == expected


def test_calculate_invalid_tax():
    with pytest.raises(ValueError):
        calculate_tax(100, -1)


def test_calculate_invalid_price():
    with pytest.raises(ValueError):
        calculate_tax(0, 10)
