import pytest
from src.task2 import calculate_tax


@pytest.mark.parametrize(
    "price, tax_rate, expected",
    [(100, 10, 110), (200, 30, 260), (300, 10, 330), (100, 20, 120)],
)
def test_calculate_tax(price, tax_rate, expected):
    calculate_tax(price, tax_rate) == expected


@pytest.mark.parametrize(
    "price, tax_rate, discount, expected",
    [(100, 10, 10, 99), (200, 30, 50, 130), (300, 10, 0, 330), (100, 20, 100, 0)],
)
def test_calculate_tax_discount(price, tax_rate, discount, expected):
    calculate_tax(price, tax_rate, discount) == expected


def test_calculate_tax_discount_under_zero():
    with pytest.raises(ValueError):
        calculate_tax(100, 10, -10)


def test_caclcutate_tax_discount_after_100():
    with pytest.raises(ValueError):
        calculate_tax(100, 10, 101)


def test_calculate_tax_invalid_tax():
    with pytest.raises(ValueError):
        calculate_tax(100, -1)


def test_calculate_tax_invalid_price():
    with pytest.raises(ValueError):
        calculate_tax(0, 10)


def test_calculate_tax_round():
    assert calculate_tax(123, 10, 15, 0) == 115.00


def test_calculate_tax_incorrect_arguments():
    with pytest.raises(TypeError):
        calculate_tax('123', 2)
