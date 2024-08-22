import pytest
from src.task1 import calculate_taxes


def test_calculate_taxes():
    assert calculate_taxes([100.0, 200.0, 300.0], 10.0) == [110.0, 220.0, 330.0]
    assert calculate_taxes([], 0) == []
    assert calculate_taxes([11.11], 1) == [11.2211]
    with pytest.raises(ValueError):
        calculate_taxes([1, 2, 3], -1)
        calculate_taxes([-1, -2], 0)
